from __future__ import annotations

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

    with patch("requests.post", return_value=FakeResponse()):
        result = GraphQL.search("title", id="tt1234567")
        assert result.data["id"] == "tt1234567"

    error_data = {"errors": [{"message": "bad query"}]}

    class FakeErrorResponse:
        content = orjson.dumps(error_data)

        @staticmethod
        def raise_for_status():
            return None

    with patch("requests.post", return_value=FakeErrorResponse()):
        with pytest.raises(ValueError, match="Query failed"):
            GraphQL.search("title", id="tt1234567")


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
