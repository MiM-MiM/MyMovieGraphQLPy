
from MyMovieGraphQL import GetByID, GraphQL, Search
from MyMovieGraphQL.MyMovie import MyMovie
import os, sys, json
import inspect
from types import UnionType, FunctionType
from typing import Any

if __name__ != '__main__':
    raise RuntimeError("This is not to be called indirectly.")

HELP = f"""
\033[4mMyMovieGraphQL\033[0m is a simplified interface for generating the GraphQL
requests to IMDb (Internet Movie Database). Calling the module directly
is capable of simple searches and fetching by ID. Returned to stdout
as json. Further abilities can be done using the module directly.
Commands are case insensitive.

Environment Variables:
    • \033[4mMYMOVIEGRAPHQL_COUNTRY\033[0m: Change the country used in the API call, default US.
    • \033[4mMYMOVIEGRAPHQL_LANGUAGE\033[0m: Change the language used in the API call, default en.
    • \033[4mMYMOVIEGRAPHQL_INDENT\033[0m: Change the indent size, defualt 2. 0 Disables indentation.

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
"""

if len(sys.argv) == 1:
    sys.stdout.write(HELP)
    sys.exit(0)

COUNTRY = os.environ.get('MYMOVIEGRAPHQL_COUNTRY', 'US')
LANGUAGE = os.environ.get('MYMOVIEGRAPHQL_LANGUAGE', 'en')
INDENT = os.environ.get('MYMOVIEGRAPHQL_INDENT', 2)

if isinstance(INDENT, str):
    try:
        INDENT = int(INDENT)
    except ValueError:
        INDENT = 4
INDENT=max(0,INDENT)

GraphQL.setLocalCountryLanguage(country=COUNTRY, language=LANGUAGE)



def getByID() -> MyMovie:
    if len(sys.argv) != 3:
        raise RuntimeError(f"GetByID requires exactly one additional argument, {len(sys.argv)-2} given.\n`MovieGraphQL getByID tt1234567`")
    return GetByID.getByID(sys.argv[2])


def search() -> MyMovie:
    if len(sys.argv) < 3:
        raise RuntimeError("Search requires at least the search term, followed by the arguments: `MovieGraphQL search term arg1=val1 arg2=val2 ...`")
    term = sys.argv[2]
    args: dict[str, Any] = get_args(Search.search)
    return Search.search(term=term, **args)

def nameSearch() -> MyMovie:
    if len(sys.argv) < 3:
        raise RuntimeError("Name search requires at least the search term, followed by the arguments: `MovieGraphQL searchName name arg1=val1 arg2=val2 ...`")
    term = sys.argv[2]
    args: dict[str, Any] = get_args(Search.searchName)
    return Search.searchName(name=term, **args)

def titleSearch() -> MyMovie:
    if len(sys.argv) < 3:
        raise RuntimeError("Title search requires at least the search term, followed by the arguments: `MovieGraphQL searchName title arg1=val1 arg2=val2 ...`")
    term = sys.argv[2]
    args: dict[str, Any] = get_args(Search.searchTitle)
    return Search.searchTitle(title=term, **args)

def update() -> MyMovie:
    if len(sys.argv) < 3:
        raise RuntimeError(f"Update requires at least one additional argument, {len(sys.argv)-2} given.\n`MovieGraphQL update key1 key2`. The current data is input using stdin.")
    data = json.loads(sys.stdin.read())
    if not (data.get('__typename') or data.get('id')):
        raise ValueError("The given input does not contain a type and id.")
    obj = MyMovie(data)
    for upd in sys.argv[2:]:
        obj.update(upd.strip())
    return obj

def get_args(func: FunctionType) -> dict[str, Any]:
    args_input = {}
    for input_arg in sys.argv[3:]:
        arg = input_arg.split("=")
        if len(arg) < 2:
            continue
        args_input[arg[0].strip().lower()] = "=".join(arg[1:]).strip()
    args = {}
    sig = inspect.signature(func)
    for param_name, param in sig.parameters.items():
        if param_name.lower() not in args_input:
            continue
        if isinstance(param.annotation, UnionType):
            args[param_name] = args_input[param_name.lower()]
        elif param.annotation == bool:
            args[param_name] = args_input[param_name.lower()].lower() not in {'f', 'false', '0'}
        else:
            args[param_name] = param.annotation(args_input[param_name.lower()])
    return args

obj = MyMovie({'__typename': 'None'})
match sys.argv[1].lower():
    case 'getbyid':
        obj = getByID()
    case 'search':
        obj = search()
    case 'namesearch' | 'searchname':
        obj = nameSearch()
    case 'titlesearch' | 'searchtitle':
        obj = titleSearch()
    case 'update':
        obj = update()
    case 'help':
        sys.stdout.write(HELP)
        sys.exit(0)
    case _:
        raise ValueError(f"Invalid selection: {sys.argv[1]}")
as_json = json.dumps(obj.to_dict(), indent=INDENT)
sys.stdout.write(as_json)
