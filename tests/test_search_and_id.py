from __future__ import annotations

from unittest.mock import patch

import pytest

from MyMovieGraphQL import GetByID, Search
from MyMovieGraphQL.MyMovie import MyMovie


def test_search_wrappers_call_graphql_search():
    result = MyMovie(
        {
            "__typename": "TitleConnection",
            "edges": [
                {
                    "node": {
                        "entity": {
                            "__typename": "Title",
                            "id": "tt0000001",
                            "titleText": "Example",
                        }
                    }
                }
            ],
        }
    )

    with patch("MyMovieGraphQL.GraphQL.search", return_value=result) as search_mock:
        returned = Search.searchTitle(title="Example", limit=10)
        assert returned == result
        search_mock.assert_called_once()

    with patch("MyMovieGraphQL.GraphQL.search", return_value=result) as search_mock:
        returned = Search.searchName(name="Example", limit=10)
        assert returned == result
        search_mock.assert_called_once()

    with patch("MyMovieGraphQL.GraphQL.search", return_value=result) as search_mock:
        returned = Search.search(term="Example", limit=10, searchType=["TITLE"], titleType=["MOVIE"])
        assert returned == result
        search_mock.assert_called_once()


def test_get_by_id_dispatches_supported_patterns():
    with patch(
        "MyMovieGraphQL.GraphQL.search",
        return_value=MyMovie(
            {
                "__typename": "Title",
                "id": "tt0000001",
                "titleText": "Example",
                "releaseYear": 2001,
            }
        ),
    ) as search_mock:
        result = GetByID.getByID("tt0000001")
        assert result.data["id"] == "tt0000001"
        search_mock.assert_called_once_with("title", id="tt0000001")

    with patch(
        "MyMovieGraphQL.GraphQL.search",
        return_value=MyMovie(
            {
                "__typename": "Name",
                "id": "nm0000001",
                "nameText": {"text": "Example Name"},
            }
        ),
    ) as search_mock:
        result = GetByID.getByID("nm0000001")
        assert result.data["id"] == "nm0000001"
        search_mock.assert_called_once_with("name", id="nm0000001")

    with pytest.raises(ValueError, match="Unknown ID format"):
        GetByID.getByID("bad")
