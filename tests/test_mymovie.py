from __future__ import annotations

from MyMovieGraphQL.MyMovie import MyMovie


def test_mymovie_wraps_nested_data_and_serializes_recursively():
    raw = {
        "__typename": "Title",
        "id": "tt1234567",
        "titleText": {"__typename": "TitleText", "text": "Example"},
        "genres": [{"__typename": "TitleGenre", "genre": "Drama"}],
    }

    movie = MyMovie(raw)

    # fmt: off
    assert movie.ofType == "Title"
    assert movie["id"] == "tt1234567"
    assert movie["titleText"].get("text") == "Example"  # pyright: ignore[reportAttributeAccessIssue]
    assert movie["genres"][0].get("genre") == "Drama"
    assert movie.to_dict()["titleText"]["text"] == "Example"
    assert bool(movie) is True
    # fmt: on


def test_mymovie_connection_behavior_and_equality():
    left = MyMovie(
        {
            "__typename": "Title",
            "id": "tt0000001",
            "titleText": "Example",
            "releaseYear": 1999,
        }
    )
    right = MyMovie(
        {
            "__typename": "Title",
            "id": "tt0000001",
            "titleText": "Example",
            "releaseYear": 1999,
        }
    )
    other = MyMovie(
        {
            "__typename": "Title",
            "id": "tt0000002",
            "titleText": "Other",
            "releaseYear": 2000,
        }
    )

    assert left == right
    assert left != other
    assert hash(left) == hash(right)
    assert str(left) == "Example (1999)"

    connection = MyMovie(
        {
            "__typename": "TitleGenreConnection",
            "edges": [
                {"node": {"__typename": "TitleGenre", "genre": "Drama"}},
                {"node": {"__typename": "TitleGenre", "genre": "Comedy"}},
            ],
        }
    )

    assert len(connection) == 2
    items = list(connection)  # pyright: ignore[reportArgumentType]
    assert [item.get("genre") for item in items] == ["Drama", "Comedy"]

    merged = left + right
    assert merged == left

    left["custom_key"] = "value"
    assert left["custom_key"] == "value"


def test_mymovie_helper_methods_and_string_rendering():
    empty = MyMovie({"__typename": "Title", "id": "tt0000003", "titleText": None})
    assert bool(empty) is False

    numeric = MyMovie({"__typename": "Title", "id": "tt0000004", "value": 42})
    assert int(numeric) == 42
    assert float(numeric) == 42.0

    title = MyMovie(
        {
            "__typename": "Title",
            "id": "tt0000005",
            "titleText": "Example",
            "releaseYear": 2001,
        }
    )
    assert str(title) == "Example (2001)"

    name = MyMovie(
        {
            "__typename": "Name",
            "id": "nm0000005",
            "nameText": "Example Name",
            "deathStatus": "ALIVE",
            "birthDate": {"date": "1990-01-01"},
        }
    )
    assert str(name) == "Example Name (1990-01-01)"

    connection = MyMovie(
        {
            "__typename": "TitleConnection",
            "edges": [
                {"node": {"__typename": "Title", "titleText": "Alpha"}},
                {"node": {"__typename": "Title", "titleText": "Beta"}},
            ],
        }
    )
    assert connection[0] == "Alpha"
    assert len(connection) == 2
