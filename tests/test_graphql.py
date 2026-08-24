from __future__ import annotations

import hashlib
from unittest.mock import patch

import orjson
import pytest

from MyMovieGraphQL import GraphQL, Search


def test_sanitize_argument_dict_removes_only_empty_nested_values():
    args = {
        "first": 10,
        "filters": {"type": None, "value": {"term": None}},
        "keep": {"present": 1},
    }

    result = GraphQL.sanatizeArgumentDict(args)

    assert result["first"] == 10  # pyright: ignore[reportOptionalSubscript]
    assert result["keep"] == {"present": 1}  # pyright: ignore[reportOptionalSubscript]
    assert result["filters"] is None  # pyright: ignore[reportOptionalSubscript]


def test_set_local_country_language_updates_headers_and_validates_input():
    original = GraphQL.HEADERS.copy()

    try:
        GraphQL.setLocalCountryLanguage("CA", "fr")
        assert GraphQL.HEADERS["x-imdb-user-country"] == "CA"
        assert GraphQL.HEADERS["x-imdb-user-language"].startswith("fr")

        with pytest.raises(ValueError, match="invalid"):
            GraphQL.setLocalCountryLanguage("ZZ", "xx")
    finally:
        GraphQL.HEADERS.clear()
        GraphQL.HEADERS.update(original)


def test_non_network_graphql_helpers():
    GraphQL.load_config_json()
    assert GraphQL.isScalarOrEnum({"kind": "SCALAR"}) is True
    assert GraphQL.isScalarOrEnum({"kind": "OBJECT"}) is False
    assert GraphQL.sanatizeArgumentDict({"a": {"b": None}, "c": 1}) == {
        "a": None,
        "c": 1,
    }


def test_graphql_search_success_and_error_paths():
    fake_data = {
        "data": {
            "query": {"__typename": "Title", "id": "tt1234567", "titleText": "Example"}
        }
    }

    class FakeResponse:
        content = orjson.dumps(fake_data)

        @staticmethod
        def raise_for_status():
            return None

    with (
        patch("requests.get", return_value=FakeResponse()),
        patch("requests.post") as post,
    ):
        result = GraphQL.search("title", id="tt1234567")
        assert result.data["id"] == "tt1234567"
        post.assert_not_called()

    error_data = {"errors": [{"message": "bad query", "extensions": None}]}

    class FakeErrorResponse:
        content = orjson.dumps(error_data)

        @staticmethod
        def raise_for_status():
            return None

    with (
        patch("requests.get", return_value=FakeErrorResponse()),
        patch("requests.post") as post,
    ):
        with pytest.raises(ValueError, match="Query failed"):
            GraphQL.search("title", id="tt1234567")
        post.assert_not_called()


def test_graphql_search_registers_persisted_query_on_cache_miss():
    cache_miss = {
        "errors": [
            {
                "message": "PersistedQueryNotFound",
                "extensions": {"code": "PERSISTED_QUERY_NOT_FOUND"},
            }
        ]
    }
    success = {"data": {"query": {"id": "tt1234567"}}}

    class FakeResponse:
        def __init__(self, payload):
            self.content = orjson.dumps(payload)

        @staticmethod
        def raise_for_status():
            return None

    with (
        patch("requests.get", return_value=FakeResponse(cache_miss)) as get,
        patch("requests.post", return_value=FakeResponse(success)) as post,
    ):
        result = GraphQL.search(
            "title", limitAttributes=["id"], id="tt1234567"
        )

    assert result.data["id"] == "tt1234567"
    get.assert_called_once()
    post.assert_called_once()

    get_request = get.call_args.kwargs
    post_request = post.call_args.kwargs
    payload = post_request["json"]
    persisted_query = payload["extensions"]["persistedQuery"]

    assert get_request["url"] == GraphQL.API_URL
    assert get_request["params"]["operationName"] == "query"
    assert "query" not in get_request["params"]
    variables = orjson.loads(get_request["params"]["variables"])
    extensions = orjson.loads(get_request["params"]["extensions"])
    assert variables["id"] == "tt1234567"
    assert extensions == payload["extensions"]
    assert payload["operationName"] == "query"
    assert persisted_query["version"] == 1
    assert persisted_query["sha256Hash"] == hashlib.sha256(
        payload["query"].encode("utf-8")
    ).hexdigest()
    assert get_request["headers"] is GraphQL.HEADERS
    assert post_request["headers"] is GraphQL.HEADERS
    assert GraphQL.HEADERS["Accept"] == (
        "application/graphql+json, application/json"
    )
    assert GraphQL.HEADERS["Origin"] == "https://www.imdb.com"
    assert GraphQL.HEADERS["x-imdb-client-name"] == "imdb-web-next-localized"


def test_graphql_query_generation_for_known_types():
    query, variables = GraphQL.generateSearch("mainSearch")

    assert "query" in query
    assert "mainSearch" in query
    assert isinstance(variables, dict)
    assert variables

    subquery, subvars = GraphQL.generateQuery("Title", limitAttributes=["titleText"])
    assert "titleText" in subquery
    assert isinstance(subvars, dict)


def test_sort_builds_expected_search_sort():
    assert Search.sort("RANKING", "DESC") == {"sortBy": "RANKING", "sortOrder": "DESC"}
    assert Search.sort("", "DESC") is None
