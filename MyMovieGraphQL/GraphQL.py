"""GraphQL helpers used to build and execute IMDb GraphQL requests.

This module contains utilities to load introspection/configuration JSON,
generate queries and searches, and execute them against IMDb's GraphQL
endpoint.
"""

from __future__ import annotations

import hashlib
import importlib.resources as resources
import json
import logging
import os
import re
import time
from datetime import date

import orjson
import requests
from beartype import beartype
from langcodes import Language

from .Constants import API_URL
from .logger import logger
from .MyMovie import MyMovie
from .UserAgent import get_user_agent
from .ValidateResponse import validate_graphql_response

MAX_RESPONSE_MIB = int(os.environ.get("MYMOVIEGRAPHQL_MAX_RESPONSE_MIB", 32))
if MAX_RESPONSE_MIB <= 0:
    raise ValueError("MYMOVIEGRAPHQL_MAX_RESPONSE_MIB must be a positive integer number of MiB.")
MAX_RESPONSE_BYTES = MAX_RESPONSE_MIB * 1024 * 1024
HEADERS = {
    "Content-Type": "application/json",
    "x-imdb-user-country": "US",
    "x-imdb-user-language": "en-US",
    "x-imdb-client-name": "imdb-web-next-localized",
    "User-Agent": get_user_agent(),
    "Connection": "close",
    "Accept": "application/graphql+json, application/json",
    "Origin": "https://www.imdb.com",
    "Referer": "https://imdb.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Accept-Encoding": "gzip, deflate",  # brotli on average seems to make it slower on average, disabled.
}
# x-imdb-customer-id

DATA, LIMITED = {}, {}
_KNOWN_PERSISTED_QUERIES: set[tuple[str, str]] = set()


def load_config_json():
    """Load the config JSON files only once."""
    global DATA, LIMITED
    # orjson is slower reading the config
    if not (DATA or LIMITED):
        logger.debug("Loading config introspection JSON config files.")
        with resources.open_text("MyMovieGraphQL.data", "INTROSPECTION.json") as f:
            DATA = json.load(f)
        with resources.open_text("MyMovieGraphQL.data", "LIMITED.json") as f:
            LIMITED = json.load(f)


@beartype
def setLocalCountryLanguage(
    country: str = HEADERS.get("x-imdb-user-country", "US"),
    language: str = HEADERS.get("x-imdb-user-language", "en-US"),
) -> None:
    """Set local country and language headers used for API requests.

    Args:
        country (str): ISO country code (defaults to HEADERS setting).
        language (str): Language code (defaults to HEADERS setting).

    Raises:
        ValueError: If the country/language combination is invalid.
    """
    global HEADERS
    if not (country and language):
        raise ValueError(f"Both the country and the language must be set, given: '{country=}', '{language=}'.")
    country = country.upper()
    # Remove country code from language.
    language = language.split("-")[0]
    # If the country isn't '-' (disabled) or "XOR" (original), validate the code.
    lang = Language.make(language=language, territory=country if country not in ["-", "XOR"] else None)
    if not lang.is_valid():
        raise ValueError(f"The given country/language combination is invalid: {lang}")
    HEADERS |= {
        "x-imdb-user-country": country,
        "x-imdb-user-language": str(lang),
    }
    logger.debug(
        "Set local country and language headers to: country=%s, language=%s",
        country,
        str(lang),
    )


@beartype
def sanatizeArgumentDict(args: dict, base: bool = True) -> dict | None:
    """Recursively sanitize argument dicts by collapsing empty children to ``None``.

    Args:
        args (dict): The arguments being sanitized.
        base (bool): When True, the top-level dict is always returned even if
            it contains no non-empty values.

    Returns:
        dict | None: The sanitized dict or ``None`` when the dict and all
        children are empty and ``base`` is False.
    """
    cleaned = args.copy()
    allMissing = True
    for key, value in cleaned.items():
        if isinstance(value, dict):
            nested = sanatizeArgumentDict(value, base=False)
            cleaned[key] = nested
            if nested:
                allMissing = False
        elif value is not None:
            allMissing = False
    if not allMissing and not base:
        for key, value in list(cleaned.items()):
            if value is None:
                del cleaned[key]
    if base:
        return cleaned
    return cleaned if not allMissing else None


@beartype
def isScalarOrEnum(obj: dict):
    """Return True if the object's kind is ``ENUM`` or ``SCALAR``.

    Args:
        obj (dict): The introspection dict describing the type.
    """
    # The return will handle attribute erors.
    return obj["kind"] in ["ENUM", "SCALAR"]


@beartype
def _persisted_query_not_found(errors: list[dict]) -> bool:
    for error in errors:
        code = (error.get("extensions") or {}).get("code")
        if code == "PERSISTED_QUERY_NOT_FOUND":
            return True
        if error.get("message") == "PersistedQueryNotFound":
            return True
    return False


@beartype
def _default_query_value(
    var: str = "",
    variable_type: str = "",
):
    """Return the default value for a GraphQL variable when it is omitted."""
    if "!" in variable_type:
        var_clean_name = re.sub(r"[\[\]\!]", "", variable_type)
        match var_clean_name:
            case "Int":
                return 25
            case "String":
                return "Missing"
            case "Boolean":
                return True
            case "Float":
                return 0.0
            case "Date":
                return str(date.today())
            case _:
                if var_clean_name in DATA:
                    var_data = DATA[var_clean_name]
                    if var_data["kind"] == "ENUM":
                        return var_data["enumValues"][0]["name"]
                    raise ValueError(f"Variable `{var}` must be filled out, of type `{var_clean_name}`")
                raise ValueError(f"Variable `{var}` has an unknown type `{var_clean_name}`")
    return None


@beartype
def _build_query_variables(
    variables: dict[str, str] | None = None,
    kwargs: dict | None = None,
) -> dict:
    """Populate GraphQL query variables using either provided kwargs or defaults."""
    if variables is None:
        variables = {}
    if kwargs is None:
        kwargs = {}
    query_variables = {}
    for var, variable_type in variables.items():
        if var in kwargs:
            query_variables[var] = kwargs[var]
            continue
        if var.endswith("_first"):
            query_variables[var] = None
            if var.replace("_first", "_last") not in kwargs:
                query_variables[var] = 25
            continue
        if var.endswith("_last"):
            query_variables[var] = None
            var_as_first = var.replace("_last", "_first")
            if var_as_first not in kwargs and var_as_first not in variables:
                query_variables[var] = 25
            continue
        query_variables[var] = _default_query_value(var, variable_type)
    query_variables = sanatizeArgumentDict(query_variables, True)
    return query_variables  # pyright: ignore[reportReturnType]


@beartype
def _summarize_query_variables(variables: dict) -> str:
    """Return a compact, non-sensitive summary of GraphQL variables."""
    if not variables:
        return "none"
    names = sorted(variables)
    return f"{len(names)} variable(s): {', '.join(names)}"


@beartype
def _prepare_search_request(
    searchName: str,
    limitAttributes: str | list[str] = "",
    **kwargs,
) -> tuple[str, dict]:
    """Build the GraphQL query and variables for a search request."""
    load_config_json()
    if limitAttributes and isinstance(limitAttributes, str):
        limitAttributes = [str(limitAttributes)]
    elif not limitAttributes:
        limitAttributes = []
    query, variables = generateSearch(searchName, limitAttributes=limitAttributes)  # type: ignore[arg-type]
    query_variables = _build_query_variables(variables, kwargs)
    return query, query_variables


@beartype
def _log_search_start(searchName: str, query_variables: dict) -> None:
    """Log a compact summary of the query context before the request is sent."""
    logger.info("Executing search '%s'.", searchName)
    logger.debug("Variables: %s", _summarize_query_variables(query_variables))
    return


@beartype
def _request_graphql_response(query_arg: dict, use_get: bool = False) -> bytes:
    """Send the GraphQL request and return the raw response body."""
    try:
        if use_get:
            response = requests.get(
                url=API_URL,
                params={
                    "operationName": query_arg["operationName"],
                    "variables": orjson.dumps(query_arg["variables"]).decode("utf-8"),
                    "extensions": orjson.dumps(query_arg["extensions"]).decode("utf-8"),
                },
                headers=HEADERS,
                timeout=(3.05, 10),
            )
        else:
            response = requests.post(
                url=API_URL,
                json=query_arg,
                headers=HEADERS,
                timeout=(3.05, 10),
            )
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            if use_get:
                try:
                    payload = _decode_graphql_response(response.content)
                except ValueError:
                    pass
                else:
                    if _persisted_query_not_found(payload.get("errors") or []):
                        return response.content
            raise
    except requests.exceptions.Timeout as exc:
        raise TimeoutError("IMDb API request timed out after 10 seconds while waiting for a response.") from exc
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"IMDb API request failed: {exc}") from exc
    return response.content


@beartype
def _decode_graphql_response(response_body: bytes) -> dict:
    """Validate response size and decode the JSON payload."""
    response_len = len(response_body)
    if response_len == 0:
        raise ValueError("GraphQL response was an empty response.")
    if response_len > MAX_RESPONSE_BYTES:
        raise ValueError(
            "GraphQL response exceeded the maximum allowed size of "
            f"{MAX_RESPONSE_BYTES} bytes ({response_len} bytes received)."
        )
    try:
        payload = orjson.loads(response_body)
    except orjson.JSONDecodeError as exc:
        raise ValueError(f"GraphQL response was not valid JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("GraphQL response did not decode to a JSON object.")
    return payload


@beartype
def _log_response_size(response_len: int, start_time: float, end_time: float) -> None:
    """Emit a compact timing and size summary for the API response."""
    if logger.isEnabledFor(logging.DEBUG):
        execution_time = end_time - start_time
        logger.debug(
            "API Response: %.2f KiB (%d Bytes) in %.6f seconds",
            response_len / 1024,
            response_len,
            execution_time,
        )
    else:
        logger.info("API Response: %.2f KiB", response_len / 1024)
    return


@beartype
def _raise_for_graphql_errors(payload: dict) -> None:
    """Raise a ValueError when the GraphQL payload indicates server-side errors."""
    errors = payload.get("errors")
    if not errors:
        return
    error_messages = "\n".join(str(error) for error in errors)
    raise ValueError(f"Query failed to execute ({len(errors)} errors):\n{'-'*40}\n{error_messages}\n{'-'*40}")


@beartype
def search(searchName: str, limitAttributes: str | list[str] = "", **kwargs) -> MyMovie:
    """Generate and execute the given search/query.

    Args:
        searchName (str): The query name to run.
        limitAttributes (str | list[str]): Optional list of attribute names to
            limit the returned fields.
        **kwargs: Additional variables passed to the query.

    Returns:
        MyMovie: The search result wrapped in a ``MyMovie`` object.
    """
    operation_name = "query"
    query, query_variables = _prepare_search_request(
        searchName,
        limitAttributes=limitAttributes,
        **kwargs,
    )
    query_hash = hashlib.sha256(query.encode("utf-8")).hexdigest()
    extensions = {
        "persistedQuery": {
            "version": 1,
            "sha256Hash": query_hash,
        }
    }
    query_arg = {
        "operationName": operation_name,
        "variables": query_variables,
        "extensions": extensions,
    }
    cache_key = (API_URL, query_hash)
    use_get = cache_key in _KNOWN_PERSISTED_QUERIES
    if not use_get:
        query_arg["query"] = query

    _log_search_start(searchName, query_variables)
    start_time = time.perf_counter()
    response_body = _request_graphql_response(query_arg, use_get=use_get)
    payload = _decode_graphql_response(response_body)
    if use_get and _persisted_query_not_found(payload.get("errors") or []):
        _KNOWN_PERSISTED_QUERIES.discard(cache_key)
        logger.debug(
            "Persisted query cache miss for '%s'; registering query.",
            searchName,
        )
        query_arg["query"] = query
        response_body = _request_graphql_response(query_arg)
        payload = _decode_graphql_response(response_body)
    end_time = time.perf_counter()
    _log_response_size(len(response_body), start_time, end_time)
    _raise_for_graphql_errors(payload)
    query_data = validate_graphql_response(payload)
    _KNOWN_PERSISTED_QUERIES.add(cache_key)
    return MyMovie(query_data)


@beartype
def _resolve_search_definition(searchName: str) -> tuple[str, dict]:
    """Resolve the canonical search name and metadata for a query."""
    load_config_json()
    search_name_lower = searchName.lower()
    for query in DATA["Query"]["fields"]:
        if query["name"].lower() == search_name_lower:
            return query["name"], query
    raise ValueError(f"{searchName} is not a valid search.")


@beartype
def _as_query_variable_type(field_type: str, is_list: bool, is_nullable: bool) -> str:
    """Convert a GraphQL type description into a concrete variable type string."""
    arg_type = field_type
    if is_list:
        arg_type = f"[{arg_type}]"
    if not is_nullable:
        arg_type = f"{arg_type.replace(']', '!]')}!"
    return arg_type


@beartype
def _build_search_variable_metadata(
    query: dict,
    sub_query_variables: dict,
) -> tuple[list[str], list[str], dict[str, str]]:
    """Build the GraphQL input variable declarations for a search query."""
    input_variables: list[str] = []
    input_variables_types: list[str] = []
    variables: dict[str, str] = {}

    for arg in query["args"]:
        arg_name = arg["name"]
        arg_type = _as_query_variable_type(arg["type"], arg["list"], arg["nullable"])
        variables[arg_name] = arg_type
        input_variables.append(f"{arg_name}: ${arg_name}")
        input_variables_types.append(f"${arg_name}: {arg_type}")

    for sub_item in sub_query_variables.values():
        arg_name = sub_item["name"]
        arg_type = _as_query_variable_type(sub_item["type"], sub_item["list"], sub_item["nullable"])
        variables[arg_name] = arg_type
        input_variables_types.append(f"${arg_name}: {arg_type}")

    return input_variables, input_variables_types, variables


@beartype
def generateSearch(searchName: str, limitAttributes: list[str] | None = None) -> tuple[str, dict[str, str]]:
    """Generate the search query and the variables needed for a given search.

    Each response will alias the query as ``query`` allowing the search name
    to be case-insensitive.

    Args:
        searchName (str): The name of the query to run (e.g. ``mainSearch``).
        limitAttributes (list[str]): Optional list of attributes to limit the
            returned fields.

    Returns:
        tuple[str, dict[str, str]]: A tuple where the first item is the query
        string and the second is a dict mapping variable names to GraphQL
        types (e.g. ``{"var": "Int!"}``).

    Raises:
        ValueError: If the given search name is not valid.
    """
    if limitAttributes is None:
        limitAttributes = []

    search_name, query = _resolve_search_definition(searchName)
    output_type = query["type"]
    sub_query, sub_query_variables = generateQuery(output_type, limitAttributes=limitAttributes)
    input_variables, input_variables_types, variables = _build_search_variable_metadata(query, sub_query_variables)
    input_variables_str = ", ".join(input_variables)
    input_variables_types_str = ", ".join(input_variables_types)
    search_query = f"""query query({input_variables_types_str}) {{
        query: {search_name}({input_variables_str}){{ __typename {sub_query} }}
    }}"""
    return search_query, variables


@beartype
def _field_limit_names(
    object_name: str = "",
    object_data: dict | None = None,
    limitAttributes: list[str] | None = None,
) -> list[str]:
    """Resolve the field names allowed for a given object type."""
    if object_data is None:
        object_data = {}
    if limitAttributes is None:
        limitAttributes = []

    limit_data = [field["name"] for field in object_data.get("fields", [])]
    if object_name in LIMITED:
        limit_data = LIMITED[object_name]
    if limitAttributes:
        limit_data = [field["name"] for field in object_data.get("fields", []) if field["name"] in limitAttributes]
    return limit_data


@beartype
def _should_skip_field(
    field_name: str = "",
    field_type: str = "",
    allow_limited: bool = False,
    limit_data: list[str] | None = None,
) -> bool:
    """Return True when the field should be omitted from the generated query."""
    if limit_data is None:
        limit_data = []
    return "Facet" in field_type or (field_name not in limit_data and not allow_limited)


@beartype
def _render_union_field(
    object_name: str = "",
    field_name: str = "",
    field_type: str = "",
    object_variables: dict | None = None,
) -> str:
    """Render a union-typed field selection exactly as before."""
    if object_variables is None:
        object_variables = {}
    sub_query = ""
    for unionType in DATA[field_type]["possibleTypes"]:
        fragment_query, subquery_variables = generateQuery(unionType)
        object_variables.update(subquery_variables)
        sub_query = f"{sub_query} ... on {unionType} {{  __typename {fragment_query} }}"
    return f"{object_name}_{field_name}: {field_name} {{ {sub_query} }}"


@beartype
def _render_args_field(
    object_name: str = "",
    field_name: str = "",
    field_type: str = "",
    args: list[dict] | None = None,
    object_variables: dict | None = None,
) -> str:
    """Render a field that takes arguments exactly as before."""
    if args is None:
        args = []
    if object_variables is None:
        object_variables = {}
    sub_query, subquery_variables = generateQuery(field_type)
    object_variables.update(subquery_variables)
    for arg in args:
        variable = f"{object_name}_{field_name}_{arg['name']}"
        object_variables[variable] = {
            "type": arg["type"],
            "nullable": arg["nullable"],
            "list": arg["list"],
            "name": variable,
        }
    arg_query = ", ".join([f"{arg['name']}: ${object_name}_{field_name}_{arg['name']}" for arg in args])
    return f"{object_name}_{field_name}: {field_name}({arg_query}) " f"{{ __typename {sub_query} }}"


@beartype
def _render_nested_field(
    object_name: str = "",
    field_name: str = "",
    field_type: str = "",
    object_variables: dict | None = None,
) -> str:
    """Render a nested object field exactly as before."""
    if object_variables is None:
        object_variables = {}
    sub_query, subquery_variables = generateQuery(field_type)
    object_variables.update(subquery_variables)
    return f"{object_name}_{field_name}: {field_name} {{ __typename {sub_query} }}"


@beartype
def _field_render_kind(
    field_type: str = "",
    args: list[dict] | None = None,
) -> str:
    """Classify the field rendering path without branching in the outer function."""
    if args:
        return "args"
    if DATA.get(field_type, {}).get("possibleTypes"):
        return "union"
    if isScalarOrEnum(DATA.get(field_type, {})):
        return "scalar"
    return "nested"


@beartype
def _render_field_selection(
    object_name: str = "",
    field: dict | None = None,
    object_variables: dict | None = None,
    allow_limited: bool = False,
    limit_data: list[str] | None = None,
) -> str | None:
    """Render one GraphQL field selection while preserving the original output."""
    if field is None:
        return None
    if object_variables is None:
        object_variables = {}
    if limit_data is None:
        limit_data = []

    field_name = field["name"]
    field_type = field["type"]
    args = field["args"]

    if _should_skip_field(field_name, field_type, allow_limited, limit_data):
        return None
    if field_type not in DATA:
        return f"{object_name}_{field_name}: {field_name}"

    render_kind = _field_render_kind(field_type, args)
    if render_kind == "union":
        return _render_union_field(object_name, field_name, field_type, object_variables)
    if render_kind == "scalar":
        return f"{object_name}_{field_name}: {field_name}"
    if render_kind == "args":
        return _render_args_field(object_name, field_name, field_type, args, object_variables)
    return _render_nested_field(object_name, field_name, field_type, object_variables)


@beartype
def generateQuery(
    object_name: str,
    allow_limited: bool = False,
    limitAttributes: list[str] | None = None,
) -> tuple[str, dict]:
    """Generate the subquery for a given GraphQL type.

    Args:
        object_name (str): The object type to generate the subquery for.
        allow_limited (bool): If True, allows limited fields (skips recursive
            blocking checks).
        limitAttributes (list[str]): Optional list of attribute names to limit
            the generated fields.

    Returns:
        tuple[str, dict]: The subquery string and a dict of variables required
        for the subquery.
    """
    if limitAttributes is None:
        limitAttributes = []
    load_config_json()
    object_variables = dict()
    object_data = DATA[object_name]
    if DATA[object_name]["possibleTypes"]:
        sub_query = ""
        subquery_variables = {}
        for unionType in DATA[object_name]["possibleTypes"]:
            fragment_query, subquery_variables = generateQuery(unionType)
            object_variables = object_variables | subquery_variables
            sub_query = f"{sub_query} ... on {unionType} {{  __typename {fragment_query} }}"
        return sub_query, object_variables
    if isScalarOrEnum(object_data):
        # Custom IMDb Scalars/ENUMs
        return object_name, object_variables

    limit_data = _field_limit_names(object_name, object_data, limitAttributes)
    object_fields = []
    for field in object_data["fields"]:
        field_query = _render_field_selection(
            object_name=object_name,
            field=field,
            object_variables=object_variables,
            allow_limited=allow_limited,
            limit_data=limit_data,
        )
        if field_query is not None:
            object_fields.append(field_query)
    obj_query = " ".join(object_fields)
    return obj_query, object_variables
