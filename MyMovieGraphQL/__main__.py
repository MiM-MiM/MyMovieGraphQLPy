"""Command-line interface for the MyMovieGraphQL package.

This module implements a minimal CLI that exposes several convenience
commands (``getByID``, ``search``, ``searchName``, ``searchTitle``,
``update``) for interacting with IMDb's GraphQL API and printing JSON to
stdout.
"""

import inspect
import sys
from types import FunctionType, UnionType
from typing import Any

import orjson

from MyMovieGraphQL import GetByID, Search
from MyMovieGraphQL.Constants import INDENT
from MyMovieGraphQL.logger import logger
from MyMovieGraphQL.MyMovie import MyMovie

if __name__ != "__main__":
    raise RuntimeError("This is not to be called indirectly.")

HELP = """
\033[4mMyMovieGraphQL\033[0m is a simplified interface for generating the GraphQL
requests to IMDb (Internet Movie Database). Calling the module directly
is capable of simple searches and fetching by ID. Returned to stdout
as json. Further abilities can be done using the module directly.
Commands are case insensitive.

Environment Variables:
    • \033[4mMYMOVIEGRAPHQL_COUNTRY\033[0m: Change the country used in the API call, default US.
    • \033[4mMYMOVIEGRAPHQL_LANGUAGE\033[0m: Change the language used in the API call, default en.
    • \033[4mMYMOVIEGRAPHQL_INDENT\033[0m: Enable or disable indent, 1 (default) is on, 0 is off. Invalid values are on.
    • \033[4mMYMOVIEGRAPHQL_LOGLEVEL\033[0m: Change the log level, default INFO. Options are DEBUG, INFO, WARNING, ERROR, CRITICAL.

Commands:
    • \033[4mhelp\033[0m: Print this help message.
    • \033[4mgetByID\033[0m: Fetch by the given ID, `tt` for titles, `nm` for names, or any other fetchable type.
    • \033[4msearch\033[0m: The base search, `title` and `name` are both returned.
    • \033[4mnameSearch\033[0m: Search only names.
    • \033[4mtitleSearch\033[0m: Search only titles.
    • \033[4mupdate\033[0m: Update the object, each additional argument is a field to update.

Additional arguments:
    • Searches use the form `argument1=value1 argument2=value2 ...`
    • Updates are just the keys to be updated, `key1 key2 ...`

Example:
    • Fetch the base tt0012345 title object.
        `python -m MyMovieGraphQL getByID tt0012345`
    • Search both titles and names for Billy Madison
        `python -m MyMovieGraphQL search "Billy Madison"`
    • Search only titles for Billy Madison
        `python -m MyMovieGraphQL searchTitle "Billy Madison"`
    • Search only names for Nicolas Cage
        `python -m MyMovieGraphQL searchName "Nicolas Cage"`
    • Search only names for Nicolas Cage, restricting to only males.
        `python -m MyMovieGraphQL searchName "Nicolas Cage" gender=male`
    • Fetch by ID and then apply an update to get the akas.
        `python -m MyMovieGraphQL getByID tt0012345 | python -m MyMovieGraphQL update akas`

Disclaimer:
    This interface is provided free of charge and is not intended to be used for commercial
    and/or for profit projects. If you wish to use this implementation for that, you must
    comply with IMDb's terms for gaining access for that type.
    https://developer.imdb.com/documentation/api-documentation/getting-access/?ref_=up_next
"""  # noqa: E501

if len(sys.argv) == 1:
    sys.stdout.write(HELP)
    sys.exit(0)


def getByID() -> MyMovie:
    """Run the ``getByID`` CLI command.

    Expects exactly one additional argument: the IMDb identifier to fetch.
    """
    if len(sys.argv) != 3:
        raise RuntimeError(
            f"GetByID requires exactly one additional argument, {len(sys.argv)-2} given.\n`MovieGraphQL getByID tt1234567`"
        )
    return GetByID.getByID(sys.argv[2])


def search() -> MyMovie:
    """Run the ``search`` CLI command.

    Uses subsequent arguments as key=value pairs that are mapped into the
    corresponding function parameters for ``Search.search``.
    """
    if len(sys.argv) < 3:
        raise RuntimeError(
            "Search requires at least the search term, "
            "followed by the arguments: `MovieGraphQL search term arg1=val1 arg2=val2 ...`"
        )
    term = sys.argv[2].strip()
    args: dict[str, Any] = get_args(Search.search)
    logger.info("Main search called with term: '%s' and args: %s", term, args)
    return Search.search(term=term, **args)


def nameSearch() -> MyMovie:
    """Run the ``searchName`` CLI command.

    Uses subsequent arguments as key=value pairs mapped to ``Search.searchName``.
    """
    if len(sys.argv) < 3:
        raise RuntimeError(
            "Name search requires at least the search term, "
            "followed by the arguments: `MovieGraphQL searchName name arg1=val1 arg2=val2 ...`"
        )
    term = sys.argv[2].strip()
    args: dict[str, Any] = get_args(Search.searchName)
    logger.info("Name search called with term: '%s' and args: %s", term, args)
    return Search.searchName(name=term, **args)


def titleSearch() -> MyMovie:
    """Run the ``searchTitle`` CLI command.

    Uses subsequent arguments as key=value pairs mapped to ``Search.searchTitle``.
    """
    if len(sys.argv) < 3:
        raise RuntimeError(
            "Title search requires at least the search term, "
            "followed by the arguments: `MovieGraphQL searchName title arg1=val1 arg2=val2 ...`"
        )
    term = sys.argv[2].strip()
    args: dict[str, Any] = get_args(Search.searchTitle)
    logger.info("Title search called with term: '%s' and args: %s", term, args)
    return Search.searchTitle(title=term, **args)


def update() -> MyMovie:
    """Run the ``update`` CLI command.

    Reads a JSON object from stdin and applies update keys passed on the
    command line to fetch additional attributes.
    """
    if len(sys.argv) < 3:
        raise RuntimeError(
            "Update requires at least one additional argument, "
            f"{len(sys.argv)-2} given.\n`MovieGraphQL update key1 key2`. "
            "The current data is input using stdin."
        )
    data = orjson.loads(sys.stdin.buffer.read())
    if not (data.get("__typename") or data.get("id")):
        raise ValueError("The given input does not contain a type and id.")
    logger.info("Given initial object <--- %s: %s --->", data.get("__typename"), data.get("id"))
    obj = MyMovie(data)
    for upd in sys.argv[2:]:
        obj.update(upd.strip())
    return obj


def _parse_cli_key_values(argv: list[str] | tuple[str, ...]) -> dict[str, str]:
    """Normalize CLI arguments of the form ``key=value`` into a dict."""
    args_input: dict[str, str] = {}
    for input_arg in argv:
        arg = input_arg.split("=")
        arg_name = arg[0].strip().lower()
        if len(arg) < 2:
            logger.warning("Ignoring argument not in key=value format: '%s'", arg_name)
            continue
        if arg_name in args_input:
            logger.warning("Ignoring duplicate argument: '%s'", arg_name)
            continue
        arg_value = "=".join(arg[1:]).strip()
        if not arg_value:
            logger.warning("Ignoring argument with no value: '%s'", arg_name)
            continue
        args_input[arg_name] = arg_value
    return args_input


def _coerce_cli_value(param_name: str, value: str, annotation: Any) -> Any:
    """Coerce a CLI value to the annotation used by the target function."""
    if isinstance(annotation, UnionType):
        return value
    if annotation is bool:
        return value.lower() not in {"f", "false", "0"}
    return annotation(value)


def get_args(func: FunctionType) -> dict[str, Any]:
    """Parse CLI key=value args and coerce them to the target function's types.

    Args:
        func (FunctionType): The function whose signature is used to coerce
            CLI-provided values.

    Returns:
        dict[str, Any]: Keyword arguments ready to pass to ``func``.
    """
    args_input = _parse_cli_key_values(sys.argv[3:])
    args: dict[str, Any] = {}
    sig = inspect.signature(func)
    for param_name, param in sig.parameters.items():
        normalized_name = param_name.lower()
        if normalized_name not in args_input:
            continue
        args[param_name] = _coerce_cli_value(
            normalized_name,
            args_input[normalized_name],
            param.annotation,
        )
    for args_input_key in args_input.keys():
        detected_args = [arg.lower() for arg in args.keys()]
        if args_input_key.lower() not in detected_args:
            logger.warning("Ignoring unknown argument: '%s'", args_input_key)
    return args


obj = MyMovie({"__typename": "None"})
match sys.argv[1].lower():
    case "getbyid":
        obj = getByID()
    case "search":
        obj = search()
    case "namesearch" | "searchname":
        obj = nameSearch()
    case "titlesearch" | "searchtitle":
        obj = titleSearch()
    case "update":
        obj = update()
    case "help":
        sys.stdout.write(HELP)
        sys.exit(0)
    case _:
        raise ValueError(f"Invalid selection: {sys.argv[1]}")
as_json = as_json = orjson.dumps(obj.to_dict(), option=INDENT).decode("utf-8")
sys.stdout.write(as_json)
