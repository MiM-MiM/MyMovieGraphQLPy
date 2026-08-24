import inspect
from types import UnionType
from typing import Any, get_args, get_origin

import pytest
from beartype.roar import BeartypeCallHintParamViolation

from MyMovieGraphQL import Constraints, GetByID, GraphQL, Search
from MyMovieGraphQL.MyMovie import MyMovie
from MyMovieGraphQL.UserAgent import get_user_agent


def _invalid_value_for_union(args):
    """Choose a value that violates a union-type annotation."""
    valid_types = []
    for arg in args:
        arg_origin = get_origin(arg)
        valid_types.append(arg_origin if arg_origin else arg)

    if str not in valid_types:
        return "a_string"
    if int not in valid_types:
        return 123
    if list not in valid_types:
        return [1, 2]
    if dict not in valid_types:
        return {"key": "value"}
    if float not in valid_types:
        return 123.45
    return {1, 2, "a"}


def _invalid_value_for_annotation(annotation):
    """Return a value that should fail validation for a given type annotation."""
    if annotation is str:
        return 123
    if annotation is int:
        return "not_an_int"
    if annotation is list:
        return "not_a_list"
    if annotation is dict:
        return "not_a_dict"
    if annotation is bool:
        return "not_a_bool"
    if annotation is float:
        return "not_a_float"
    if get_origin(annotation) is list:
        return "not_a_list"
    return {1, 2, "a"}


def get_invalid_type_for_annotation(annotation):
    """Return a value of the wrong type for the supplied annotation."""
    if annotation is Any:
        return None

    origin = get_origin(annotation)
    args = get_args(annotation)

    if origin is UnionType:
        return _invalid_value_for_union(args)
    return _invalid_value_for_annotation(annotation)


constraint_functions = [
    (name, func)
    for name, func in inspect.getmembers(Constraints, inspect.isfunction)
    if not name.startswith("__") and name != "Any" and name != "beartype"
]
getByID_functions = [
    (name, func)
    for name, func in inspect.getmembers(GetByID, inspect.isfunction)
    if not name.startswith("__") and name != "Any" and name != "beartype"
]
graphQL_functions = [
    (name, func)
    for name, func in inspect.getmembers(GraphQL, inspect.isfunction)
    if not name.startswith("__") and name != "Any" and name != "beartype"
]
search_functions = [
    (name, func)
    for name, func in inspect.getmembers(Search, inspect.isfunction)
    if not name.startswith("__") and name != "Any" and name != "beartype"
]
all_functions = getByID_functions + constraint_functions + graphQL_functions + search_functions


@pytest.mark.parametrize("name, func", all_functions)
def test_function_typing(name, func):
    sig = inspect.signature(func)

    for param_name, param in sig.parameters.items():
        annotation = param.annotation
        if annotation is inspect.Parameter.empty:
            continue

        invalid_value = get_invalid_type_for_annotation(annotation)
        if invalid_value is None:
            continue
        kwargs = {param_name: invalid_value}

        with pytest.raises(BeartypeCallHintParamViolation):
            try:
                func(**kwargs)
            except BeartypeCallHintParamViolation:
                raise
            except Exception as e:
                args = ", ".join(f"{key}={val}" for key, val in kwargs.items())
                print(f"{name}({args})\n\t>> {e}")
                raise e


exampleMovie = MyMovie({"__typename": "Movie"})


def test_MyMovie_constructor_and_update_types():
    with pytest.raises(BeartypeCallHintParamViolation):
        MyMovie(1234)  # type: ignore

    tests = [
        {"attribute": 1234},
        {"previous": "not_a_bool"},
        {"variables": "not_a_dict"},
    ]
    for test in tests:
        with pytest.raises(BeartypeCallHintParamViolation):
            exampleMovie.update(**test)


@pytest.mark.parametrize(
    "method_name, call",
    [
        ("MyMovie.update", lambda movie: movie.update(attribute=1234)),
        ("MyMovie.__getitem__", lambda movie: movie[1.234]),
        ("MyMovie.__setitem__", lambda movie: movie.__setitem__(123, "value")),
    ],
)
def test_remaining_MyMovie_type_hints(method_name, call):
    with pytest.raises(BeartypeCallHintParamViolation):
        call(exampleMovie)


def test_MyMovie_add_and_get_set_types():
    with pytest.raises(TypeError):
        _ = exampleMovie + 5

    with pytest.raises(BeartypeCallHintParamViolation):
        exampleMovie[{1, 2}]  # type: ignore
    with pytest.raises(BeartypeCallHintParamViolation):
        exampleMovie[1.234]  # type: ignore


def test_MyMovie_numeric_bool_and_iterator_helpers():
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

    connection = MyMovie(
        {
            "__typename": "TitleConnection",
            "edges": [
                {"node": {"__typename": "Title", "titleText": "Alpha"}},
                {"node": {"__typename": "Title", "titleText": "Beta"}},
            ],
        }
    )
    assert len(connection) == 2
    assert connection[0] == "Alpha"
    # fmt: off
    assert [item.get("titleText") for item in iter(connection)] == ["Alpha", "Beta"]  # pyright: ignore[reportAttributeAccessIssue] # noqa: E501
    # fmt: on


def test_user_agent_type_contract():
    assert isinstance(get_user_agent(), str)
    assert "MyMovieGraphQL" in get_user_agent()
