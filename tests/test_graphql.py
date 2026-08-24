from __future__ import annotations

import hashlib
import logging
from pathlib import Path
from unittest.mock import patch

import orjson
import pytest
import requests

from MyMovieGraphQL import GraphQL, Search


@pytest.fixture(autouse=True)
def clear_persisted_query_cache():
    GraphQL._KNOWN_PERSISTED_QUERIES.clear()
    yield
    GraphQL._KNOWN_PERSISTED_QUERIES.clear()


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
    fake_data = {"data": {"query": {"__typename": "Title", "id": "tt1234567", "titleText": "Example"}}}

    class FakeResponse:
        content = orjson.dumps(fake_data)

        @staticmethod
        def raise_for_status():
            return None

    with patch("requests.post", return_value=FakeResponse()):
        result = GraphQL.search("title", id="tt1234567")
        assert result.data["id"] == "tt1234567"

    GraphQL._KNOWN_PERSISTED_QUERIES.clear()

    error_data = {"errors": [{"message": "bad query"}]}

    class FakeErrorResponse:
        content = orjson.dumps(error_data)

        @staticmethod
        def raise_for_status():
            return None

    with patch("requests.post", return_value=FakeErrorResponse()):
        with pytest.raises(ValueError, match="Query failed"):
            GraphQL.search("title", id="tt1234567")

    with patch("requests.post", side_effect=requests.exceptions.Timeout("timed out")):
        with pytest.raises(TimeoutError, match="timed out"):
            GraphQL.search("title", id="tt1234567")

    class OversizedResponse:
        content = b"x" * (GraphQL.MAX_RESPONSE_BYTES + 1)

        @staticmethod
        def raise_for_status():
            return None

    with patch("requests.post", return_value=OversizedResponse()):
        with pytest.raises(ValueError, match="maximum allowed size"):
            GraphQL.search("title", id="tt1234567")


def test_graphql_search_posts_unseen_hash_then_gets_seen_hash():
    first_data = {"data": {"query": {"__typename": "Title", "id": "tt1234567"}}}
    second_data = {"data": {"query": {"__typename": "Title", "id": "tt7654321"}}}

    class FakeResponse:
        def __init__(self, payload):
            self.content = orjson.dumps(payload)

        @staticmethod
        def raise_for_status():
            return None

    with (
        patch("requests.get", return_value=FakeResponse(second_data)) as get,
        patch("requests.post", return_value=FakeResponse(first_data)) as post,
    ):
        first = GraphQL.search("title", limitAttributes=["id"], id="tt1234567")
        second = GraphQL.search("title", limitAttributes=["id"], id="tt7654321")

    assert first.data["id"] == "tt1234567"
    assert second.data["id"] == "tt7654321"
    post.assert_called_once()
    get.assert_called_once()

    post_request = post.call_args.kwargs
    get_request = get.call_args.kwargs
    payload = post_request["json"]
    persisted_query = payload["extensions"]["persistedQuery"]
    query_hash = hashlib.sha256(payload["query"].encode("utf-8")).hexdigest()

    assert payload["operationName"] == "query"
    assert payload["variables"]["id"] == "tt1234567"
    assert persisted_query == {"version": 1, "sha256Hash": query_hash}
    assert (GraphQL.API_URL, query_hash) in GraphQL._KNOWN_PERSISTED_QUERIES
    assert get_request["url"] == GraphQL.API_URL
    assert get_request["params"]["operationName"] == "query"
    assert "query" not in get_request["params"]
    assert orjson.loads(get_request["params"]["variables"])["id"] == "tt7654321"
    assert orjson.loads(get_request["params"]["extensions"]) == payload["extensions"]
    assert get_request["headers"] is GraphQL.HEADERS
    assert post_request["headers"] is GraphQL.HEADERS
    assert get_request["timeout"] == (3.05, 10)
    assert post_request["timeout"] == (3.05, 10)
    assert GraphQL.HEADERS["Accept"] == "application/graphql+json, application/json"
    assert GraphQL.HEADERS["Origin"] == "https://www.imdb.com"
    assert GraphQL.HEADERS["x-imdb-client-name"] == "imdb-web-next-localized"


@pytest.mark.parametrize("http_error", [False, True])
def test_graphql_search_falls_back_when_known_hash_is_missing(http_error):
    cache_miss = {
        "errors": [
            {
                "message": "PersistedQueryNotFound",
                "extensions": {"code": "PERSISTED_QUERY_NOT_FOUND"},
            }
        ]
    }
    success = {"data": {"query": {"__typename": "Title", "id": "tt1234567"}}}

    class FakeResponse:
        def __init__(self, payload, raise_http_error=False):
            self.content = orjson.dumps(payload)
            self.raise_http_error = raise_http_error

        def raise_for_status(self):
            if self.raise_http_error:
                raise requests.exceptions.HTTPError("400 Client Error")

    query, _ = GraphQL.generateSearch("title", limitAttributes=["id"])
    query_hash = hashlib.sha256(query.encode("utf-8")).hexdigest()
    cache_key = (GraphQL.API_URL, query_hash)
    GraphQL._KNOWN_PERSISTED_QUERIES.add(cache_key)

    with (
        patch("requests.get", return_value=FakeResponse(cache_miss, http_error)) as get,
        patch("requests.post", return_value=FakeResponse(success)) as post,
    ):
        result = GraphQL.search("title", limitAttributes=["id"], id="tt1234567")

    assert result.data["id"] == "tt1234567"
    get.assert_called_once()
    post.assert_called_once()
    assert post.call_args.kwargs["json"]["query"] == query
    assert cache_key in GraphQL._KNOWN_PERSISTED_QUERIES


def test_graphql_search_does_not_post_for_other_get_errors():
    error_data = {"errors": [{"message": "bad query", "extensions": None}]}

    class FakeResponse:
        content = orjson.dumps(error_data)

        @staticmethod
        def raise_for_status():
            return None

    query, _ = GraphQL.generateSearch("title", limitAttributes=["id"])
    query_hash = hashlib.sha256(query.encode("utf-8")).hexdigest()
    GraphQL._KNOWN_PERSISTED_QUERIES.add((GraphQL.API_URL, query_hash))

    with (
        patch("requests.get", return_value=FakeResponse()),
        patch("requests.post") as post,
    ):
        with pytest.raises(ValueError, match="Query failed"):
            GraphQL.search("title", limitAttributes=["id"], id="tt1234567")

    post.assert_not_called()


def test_graphql_debug_logging_summarizes_variables(caplog):
    fake_data = {"data": {"query": {"__typename": "Title", "id": "tt1234567", "titleText": "Example"}}}

    class FakeResponse:
        content = orjson.dumps(fake_data)

        @staticmethod
        def raise_for_status():
            return None

    original_level = GraphQL.logger.level
    GraphQL.logger.setLevel(logging.DEBUG)
    try:
        with patch("requests.post", return_value=FakeResponse()):
            with caplog.at_level(logging.DEBUG):
                GraphQL.search("title", id="tt1234567")
    finally:
        GraphQL.logger.setLevel(original_level)

    assert "Variables: " in caplog.text
    assert "Validated GraphQL payload with keys" in caplog.text


def test_graphql_request_errors_and_invalid_json_are_hardened():
    class EmptyResponse:
        content = b""

        @staticmethod
        def raise_for_status():
            return None

    with patch("requests.post", return_value=EmptyResponse()):
        with pytest.raises(ValueError, match="invalid JSON|empty response"):
            GraphQL.search("title", id="tt1234567")

    with patch(
        "requests.post",
        side_effect=requests.exceptions.ConnectionError("offline"),
    ):
        with pytest.raises(RuntimeError, match="IMDb API request failed|offline"):
            GraphQL.search("title", id="tt1234567")


def test_graphql_query_generation_for_known_types():
    query, variables = GraphQL.generateSearch("mainSearch")

    assert "query" in query
    assert "mainSearch" in query
    assert isinstance(variables, dict)
    assert variables

    limited_query, limited_vars = GraphQL.generateQuery("Title", limitAttributes=["titleText"])
    assert isinstance(limited_vars, dict)
    assert "__typename" in limited_query
    assert "Title_titleText: titleText" in limited_query
    assert "Title_id: id" not in limited_query
    assert "Title_originalTitleText:" not in limited_query

    full_query, full_vars = GraphQL.generateQuery("Title")
    assert isinstance(full_vars, dict)
    assert "__typename" in full_query
    assert "Title_titleText: titleText" in full_query
    assert "Title_id: id" in full_query
    assert "Title_primaryImage: primaryImage" in full_query


def test_graphql_generate_query_title_matches_snapshot():
    snapshot_path = Path(__file__).with_name("GraphQL_generateQuery_Title.snapshot.txt")
    expected = snapshot_path.read_text(encoding="utf-8").strip()
    actual = repr(GraphQL.generateQuery("Title"))
    assert actual == expected


def test_sort_builds_expected_search_sort():
    assert Search.sort("RANKING", "DESC") == {"sortBy": "RANKING", "sortOrder": "DESC"}
    assert Search.sort("", "DESC") is None
