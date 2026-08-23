from __future__ import annotations

import inspect

import pytest

from MyMovieGraphQL import Constraints


def test_constraint_builders_can_be_invoked_with_defaults():
    funcs = [
        (name, func)
        for name, func in inspect.getmembers(Constraints, inspect.isfunction)
        if not name.startswith("__")
        and name not in {"_getFromListIfExists", "beartype"}
    ]

    for name, func in funcs:
        result = func()
        assert result is None or isinstance(
            result, dict
        ), f"{name} returned {type(result)}"


def test_basic_constraint_builders_return_expected_shapes():
    assert Constraints.textSearchConstraint("matrix") == {"searchTerm": "matrix"}
    assert Constraints.titleTypeConstraint("MOVIE") == {"anyTitleTypeIds": ["MOVIE"]}
    assert Constraints.titleTypeConstraint("MOVIE", "TV") == {
        "excludeTitleTypeIds": ["TV"]
    }

    assert Constraints.withDataConstraint(["rating", "cast"], ["plot"]) == {
        "allDataAvailable": ["RATING", "CAST"],
        "noDataAvailable": ["PLOT"],
    }

    assert Constraints.birthDateConstraint("1990-01-01", "1999-12-31", "--06-19") == {
        "birthday": "--06-19",
        "birthDateRange": {"start": "1990-01-01", "end": "1999-12-31"},
    }

    with pytest.raises(ValueError, match="start date"):
        Constraints.birthDateConstraint("bad-date")
