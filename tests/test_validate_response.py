from unittest.mock import patch

import orjson
import pytest

from MyMovieGraphQL import GraphQL
from MyMovieGraphQL.ValidateResponse import (
    ResponseValidationError,
    validate_graphql_response,
)


def test_validate_graphql_response_accepts_valid_payload():
    payload = {"data": {"query": {"__typename": "Title", "id": "tt0111168"}}}

    assert validate_graphql_response(payload) == payload["data"]["query"]


def test_validate_graphql_response_rejects_missing_query():
    with pytest.raises(ResponseValidationError):
        validate_graphql_response({"data": {}})


@patch("MyMovieGraphQL.GraphQL.requests.post")
def test_graphql_search_validates_response_before_wrapping(mock_post):
    payload = {
        "data": {
            "query": {
                "__typename": "Title",
                "id": "tt0111168",
                "titleText": {"text": "Example Title"},
            }
        }
    }
    mock_post.return_value.raise_for_status.return_value = None
    mock_post.return_value.content = orjson.dumps(payload)

    result = GraphQL.search("title", id="tt0111168")

    assert result.ofType == "Title"
    assert result.get("id") == "tt0111168"
    assert result.get("titleText").get("text") == "Example Title"
