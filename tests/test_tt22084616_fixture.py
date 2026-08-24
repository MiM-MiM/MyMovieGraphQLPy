from __future__ import annotations

import importlib.util
from pathlib import Path
from unittest.mock import patch

import orjson

from MyMovieGraphQL import GetByID
from MyMovieGraphQL.MyMovie import MyMovie

_RAW_FETCH_PATH = Path(__file__).with_name("raw_fetch_tt22084616.py")
_RAW_FETCH_SPEC = importlib.util.spec_from_file_location("raw_fetch_tt22084616", _RAW_FETCH_PATH)
assert _RAW_FETCH_SPEC is not None and _RAW_FETCH_SPEC.loader is not None
_RAW_FETCH_MODULE = importlib.util.module_from_spec(_RAW_FETCH_SPEC)
_RAW_FETCH_SPEC.loader.exec_module(_RAW_FETCH_MODULE)
_mock_graphql_dict = _RAW_FETCH_MODULE._mock_graphql_dict


FIXTURE_PATH = Path(__file__).with_name("tt22084616.json")
UPDATE_FIXTURE_PATH = Path(__file__).with_name("tt22084616_akas.json")
SECOND_UPDATE_FIXTURE_PATH = Path(__file__).with_name("tt22084616_akas_page2.json")


def test_recursive_mock_graphql_dict_keeps_typename_and_reuses_values():
    payload = {
        "__typename": "Title",
        "akas": {
            "__typename": "AkaConnection",
            "edges": [
                {
                    "node": {
                        "__typename": "Aka",
                        "text": "Spider-Man: Brand New Day",
                        "country": {
                            "__typename": "DisplayableCountry",
                            "id": "US",
                            "text": "United States",
                        },
                        "attributes": [{"__typename": "AkaAttribute", "id": "1", "text": "text1"}],
                    }
                },
                {
                    "node": {
                        "__typename": "Aka",
                        "text": "Spider-Man: Brand New Day",
                        "country": {
                            "__typename": "DisplayableCountry",
                            "id": "US",
                            "text": "United States",
                        },
                        "attributes": [{"__typename": "AkaAttribute", "id": "1", "text": "text1"}],
                    }
                },
            ],
        },
    }

    mocked = _mock_graphql_dict(payload)

    assert mocked["__typename"] == "Title"
    assert mocked["akas"]["__typename"] == "AkaConnection"
    assert mocked["akas"]["edges"][0]["node"]["text"] == mocked["akas"]["edges"][1]["node"]["text"]
    assert mocked["akas"]["edges"][0]["node"]["country"]["id"] == mocked["akas"]["edges"][1]["node"]["country"]["id"]
    assert mocked["akas"]["edges"][0]["node"]["country"]["text"] == mocked["akas"]["edges"][1]["node"]["country"]["text"]
    assert (
        mocked["akas"]["edges"][0]["node"]["attributes"][0]["id"] == mocked["akas"]["edges"][1]["node"]["attributes"][0]["id"]
    )


def test_get_by_id_tt22084616_matches_saved_fixture():
    expected = _mock_graphql_dict(orjson.loads(FIXTURE_PATH.read_bytes()))

    with patch(
        "MyMovieGraphQL.GraphQL.search",
        return_value=MyMovie(expected),
    ) as search_mock:
        result = GetByID.getByID("tt22084616")

    assert result.to_dict() == expected
    search_mock.assert_called_once_with("title", id="tt22084616")


def test_get_by_id_tt22084616_update_matches_saved_akas_fixture():
    expected = _mock_graphql_dict(orjson.loads(FIXTURE_PATH.read_bytes()))
    expected_after_first_update = _mock_graphql_dict(orjson.loads(UPDATE_FIXTURE_PATH.read_bytes()))
    partial_update = {
        "__typename": "Title",
        "akas": expected_after_first_update["akas"],
    }

    with patch(
        "MyMovieGraphQL.GraphQL.search",
        side_effect=[MyMovie(expected), MyMovie(partial_update)],
    ) as search_mock:
        result = GetByID.getByID("tt22084616")
        update = result.update("akas")

    assert update is not None
    assert result.to_dict() == expected_after_first_update
    assert update.to_dict() == partial_update
    assert search_mock.call_args_list[0].args == ("title",)
    assert search_mock.call_args_list[0].kwargs == {"id": expected["id"]}
    assert search_mock.call_args_list[1].args == ()
    assert search_mock.call_args_list[1].kwargs["searchName"] == "title"
    assert search_mock.call_args_list[1].kwargs["limitAttributes"] == "akas"
    assert search_mock.call_args_list[1].kwargs["id"] == expected["id"]


def test_get_by_id_tt22084616_second_update_matches_saved_akas_page2_fixture():
    expected = _mock_graphql_dict(orjson.loads(FIXTURE_PATH.read_bytes()))
    first_page = _mock_graphql_dict(orjson.loads(UPDATE_FIXTURE_PATH.read_bytes()))
    second_page = _mock_graphql_dict(orjson.loads(SECOND_UPDATE_FIXTURE_PATH.read_bytes()))
    second_page_partial = {
        "__typename": "Title",
        "akas": {
            "__typename": "AkaConnection",
            "edges": second_page["akas"]["edges"][25:],
            "pageInfo": second_page["akas"]["pageInfo"],
            "total": second_page["akas"]["total"],
        },
    }

    with patch(
        "MyMovieGraphQL.GraphQL.search",
        side_effect=[
            MyMovie(expected),
            MyMovie({"__typename": "Title", "akas": first_page["akas"]}),
            MyMovie(second_page_partial),
        ],
    ) as search_mock:
        result = GetByID.getByID("tt22084616")
        first_update = result.update("akas")
        assert first_update is not None
        assert result.to_dict() == first_page

        second_update = result.update("akas")

    assert second_update is not None
    assert result.to_dict() == second_page
    assert second_update.to_dict() == second_page_partial

    seen = set()
    for aka in result["akas"]:
        country = aka.get("country")
        country_id = None if country is None else country.get("id")
        language = aka.get("language")
        language_id = None if language is None else language.get("id")
        key = (
            country_id,
            aka.get("text"),
            language_id,
            tuple(sorted((attr.get("id"), attr.get("text")) for attr in aka.get("attributes", []))),
        )
        if key in seen:
            raise AssertionError(f"Duplicate aka found in combined result: {key}")
        seen.add(key)

    assert len(seen) == len(result["akas"])
    assert search_mock.call_args_list[2].kwargs["searchName"] == "title"
    assert search_mock.call_args_list[2].kwargs["limitAttributes"] == "akas"
    assert search_mock.call_args_list[2].kwargs["id"] == expected["id"]
