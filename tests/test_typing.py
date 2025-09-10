import pytest
import inspect
from beartype.roar import BeartypeCallHintParamViolation
from MyMovieGraphQL import Constraints, GetByID, GraphQL, Search
from MyMovieGraphQL.__init__ import MyMovie
from typing import get_origin, get_args, Any
from types import UnionType

def get_invalid_type_for_annotation(annotation):
    """
    Returns a value of a type that is invalid for the given annotation.
    """
    if annotation is Any:
        return None # Cannot test Any

    origin = get_origin(annotation)
    args = get_args(annotation)

    # Handle Union types (e.g., str | list[str])
    if origin is UnionType:
        valid_types = []
        for arg in args:
            arg_origin = get_origin(arg)
            if arg_origin:
                valid_types.append(arg_origin)
            else:
                valid_types.append(arg)
        
        # Find a type that is not in the valid types
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
        # Return a set
        return {1, 2, 'a'}

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
    if origin is list:
        return "not_a_list"
    # Default to return a set
    return {1, 2, 'a'}

constraint_functions = [
    (name, func) for name, func in inspect.getmembers(Constraints, inspect.isfunction)
    if not name.startswith('__') and name != "Any" and name != "beartype"
]
getByID_functions = [
    (name, func) for name, func in inspect.getmembers(GetByID, inspect.isfunction)
    if not name.startswith('__') and name != "Any" and name != "beartype"
]
graphQL_functions = [
    (name, func) for name, func in inspect.getmembers(GraphQL, inspect.isfunction)
    if not name.startswith('__') and name != "Any" and name != "beartype"
]
search_functions = [
    (name, func) for name, func in inspect.getmembers(Search, inspect.isfunction)
    if not name.startswith('__') and name != "Any" and name != "beartype"
]
all_functions = getByID_functions + constraint_functions + graphQL_functions + search_functions

@pytest.mark.parametrize("name, func", all_functions)
def test_function_typing(name, func):
    sig = inspect.signature(func)

    for param_name, param in sig.parameters.items():
        annotation = param.annotation
        if annotation is inspect.Parameter.empty:
            continue

        # Get an invalid value for the parameter's type annotation
        invalid_value = get_invalid_type_for_annotation(annotation)
        if invalid_value is None:
            continue
        kwargs = {param_name: invalid_value}

        with pytest.raises(BeartypeCallHintParamViolation):
            try:
                func(**kwargs)
            except BeartypeCallHintParamViolation as e:
                raise e
            except Exception as e:
                args = ', '.join(f"{key}={val}" for key, val in kwargs.items())
                # Simple print of the input that caused an error
                print(f"{name}({args})\n\t>> {e}")
                raise e

# Do these manually.
exampleMovie = MyMovie({'__typename': 'Movie'})
def test_MyMovie():
    with pytest.raises(BeartypeCallHintParamViolation):
        MyMovie(1234) # type: ignore
def test_MyMovie_add():
    with pytest.raises(TypeError):
        add = exampleMovie + 5
def test_MyMovie_update():
    tests = [
        {'attribute': 1234},
        {'previous': 'not_a_bool'},
        {'variables': 'not_a_dict'},
    ]
    for test in tests:
        with pytest.raises(BeartypeCallHintParamViolation):
            exampleMovie.update(**test)
def test_MyMovie_get_set():
    with pytest.raises(BeartypeCallHintParamViolation):
        exampleMovie[{1, 2}] # type: ignore
    with pytest.raises(BeartypeCallHintParamViolation):
        exampleMovie[1.234] # type: ignore
