import json
import re
import requests
from datetime import date
import importlib.resources as resources
from MyMovieGraphQL.__init__ import MyMovie

API_URL = "https://api.graphql.imdb.com/"
HEADERS = {"Content-Type": "application/json"}

DATA, LIMITED = {}, {}
def load_config_json():
    """Loads the config files only once.
    """
    global DATA, LIMITED
    if not (DATA or LIMITED):
        with resources.open_text('MyMovieGraphQL.data', 'INTROSPECTION.json') as f:
            DATA = json.load(f)
        with resources.open_text('MyMovieGraphQL.data', 'LIMITED.json') as f:
            LIMITED = json.load(f)

def sanatizeArgumentDict(args: dict, base: bool = True):
    """ Recursively sets the arguments to None if the child objects
    are also empty. The base argument object keeps

    Args:
        args(dict, required): The args being sanatized.
        base(bool, optional): The base arguments must remain even if null, this specifies that.
    """
    allMissing = True
    for arg in args:
        if isinstance(args[arg], dict):
            args[arg] = sanatizeArgumentDict(args[arg], base=False)
            if args[arg]:
                allMissing = False
        elif args[arg] is not None:
            allMissing = False
    argKeys = list(args.keys())
    if not allMissing and not base:
        for arg in argKeys:
            if args[arg] is None:
                del args[arg]
    if base:
        return args
    return args if not allMissing else None

def isScalarOrEnum(obj: dict):
    """Returns true if the object's kind is an ENUM or SCALAR (has no subfields)

    Args:
        obj(dict, required): The dict of the type from the introspection.
    """
    return obj['kind'] in ['ENUM', 'SCALAR']

def search(searchName: str, limitAttributes: str | list[str] = "", **kwargs) -> MyMovie:
    """Generates and executes the given search/query.

    Args:
        searchName (str, required): The query name to be ran.
        kwargs: The args for the query.
    """
    load_config_json()
    if limitAttributes and isinstance(limitAttributes, str):
        limitAttributes = [str(limitAttributes)]
    query, variables = generateSearch(searchName, limitAttributes=limitAttributes) # type: ignore
    query_variables = dict()
    for var in variables:
        variable_type = variables[var]
        if var in kwargs:
            query_variables[var] = kwargs[var]
        elif '!' in variable_type:
            var_clean_name = re.sub(r'[\[\]\!]', '', variable_type)
            match var_clean_name:
                case 'Int':
                    query_variables[var] = 25
                case 'String':
                    query_variables[var] = 'Missing'
                case 'Boolean':
                    query_variables[var] = True
                case 'Float':
                    query_variables[var] = 0.0
                case 'Date':
                    query_variables[var] = str(date.today())
                case _:
                    if var_clean_name in DATA:
                        var_data = DATA[var_clean_name]
                        if var_data['kind'] == 'ENUM':
                            enumValue = var_data['enumValues'][0]['name']
                            query_variables[var] = enumValue
                        else:
                            raise ValueError(f'Variable `{var}` must be filled out, of type `{var_clean_name}`')
        elif var.endswith('_first'):
            query_variables[var] = None
            if var.replace('_first', '_last') not in kwargs:
                query_variables[var] = 25
        elif var.endswith('_last'):
            query_variables[var] = None
            var_as_first = var.replace('_last', '_first')
            if var_as_first not in kwargs and var_as_first not in variables:
                query_variables[var] = 25
        else:
            query_variables[var] = None
    query_variables = sanatizeArgumentDict(query_variables, True)
    query_arg = {
        'query': query,
        'variables': query_variables
    }
    r = requests.post(url=API_URL, json=query_arg, headers=HEADERS).json()
    errors = r.get('errors')
    if errors:
        error_messages = f'\n'.join([str(e) for e in errors])
        raise ValueError(f"Query failed to execute ({len(errors)} errors):\n{'-'*40}\n{error_messages}\n{'-'*40}")
    return MyMovie(r.get('data', {}).get('query', {}))

def generateSearch(searchName: str, limitAttributes: list[str] = []) -> tuple[str, dict[str, str]]:
    """Generates the search query and needed variables for a given search.
    Each response will alias the query as `query` allowing for the searchName to be
    case insensitive.
    
    Args:
       searchName (str, required): The name of the query to run,
           i.e. mainSearch for the same type of response if typed into
           the top search bar on imdb's website.
    Returns:
        str: The query itself to be ran
        dict[str, str]: The dict of the variables:
            {variable: type}
            - variable names are prefixed to avoid colisions.
    Raises:
        ValueError: When the given search is not a valid option.
    """
    load_config_json()
    query = None
    searchName_lower = searchName.lower()
    for q in DATA['Query']['fields']:
        if q['name'].lower() == searchName_lower:
            searchName = q['name']
            query = q
            break
    if not query:
        raise ValueError(f"{searchName} is not a valid search.")
    output_type = query['type']
    sub_query, sub_query_variables = generateQuery(output_type, limitAttributes=limitAttributes)
    input_variables_types, input_variables = [], []
    variables = {}
    for arg in query['args']:
        arg_name = arg['name']
        arg_type = arg['type']
        if arg['list']:
            arg_type = f"[{arg_type}]"
        if not arg['nullable']:
            arg_type = f"{arg_type.replace(']', '!]')}!"
        variables[arg_name] = arg_type
        input_variables.append(f"{arg_name}: ${arg_name}")
        input_variables_types.append(f"${arg_name}: {arg_type}")
    for sub_var, sub_item in sub_query_variables.items():
        arg_name = sub_item['name']
        arg_type = sub_item['type']
        if sub_item['list']:
            arg_type = f"[{arg_type}]"
        if not sub_item['nullable']:
            arg_type = f"{arg_type.replace(']', '!]')}!"
        variables[arg_name] = arg_type
        input_variables_types.append(f"${arg_name}: {arg_type}")
    input_variables_str = ", ".join(input_variables)
    input_variables_types_str = f", ".join(input_variables_types)
    search_query = f"query query({input_variables_types_str}) {{ query: {searchName}({input_variables_str}){{ __typename {sub_query} }} }}"
    return search_query, variables

def generateQuery(object_name: str,
                  allow_limited: bool = False,
                  limitAttributes: list[str] = [],
) -> tuple[str, dict]:
    """ Generates the subquery for the given type.
    Args:
        object_name(str, required): the object type to use.
        allow_limited(bool, optional): default false.
            Used to skip the check of blocking recursive types.
    Returns:
        str: The subquery
        set[dict]: A set of dicts for the variables.
    """
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
    limit_data = [f['name'] for f in object_data['fields']]
    if object_name in LIMITED:
        limit_data = LIMITED[object_name]
    if limitAttributes:
        limit_data = [
            f['name']
            for f in object_data['fields']
            if f['name'] in limitAttributes
        ]
    object_fields = []
    for field in object_data['fields']:
        field_name = field['name']
        field_type = field['type']
        args = field['args']
        subquery_variables = {}
        if "Facet" in field_type:
            # XXX: Possibly implement later, this is a sub search essentially. If not passed it will error.
            continue
        if field_name not in limit_data and not allow_limited:
            # Skipped to avoid recursion issues.
            continue
        if field_type not in DATA:
            sub_query = f"{object_name}_{field_name}: {field_name}"
        elif DATA[field_type]["possibleTypes"]:
            sub_query = ""
            for unionType in DATA[field_type]["possibleTypes"]:
                fragment_query, subquery_variables = generateQuery(unionType)
                object_variables = object_variables | subquery_variables
                sub_query = f"{sub_query} ... on {unionType} {{  __typename {fragment_query} }}"
            sub_query = f"{object_name}_{field_name}: {field_name} {{ {sub_query} }}"
        elif isScalarOrEnum(DATA[field_type]):
            sub_query = f"{object_name}_{field_name}: {field_name}"
        elif args:
            sub_query, subquery_variables = generateQuery(field_type)
            for arg in args:
                variable = f"{object_name}_{field_name}_{arg['name']}"
                object_variables[variable] = {
                    'type': arg['type'],
                    'nullable': arg['nullable'],
                    'list': arg['list'],
                    'name': variable,
                }
            arg_query = ", ".join([
                f"{arg['name']}: ${object_name}_{field_name}_{arg['name']}"
                for arg in args
            ])
            sub_query = f"{object_name}_{field_name}: {field_name}({arg_query}) {{ __typename {sub_query} }}"
        else:
            sub_query, subquery_variables = generateQuery(field_type)
            sub_query = f"{object_name}_{field_name}: {field_name} {{ __typename {sub_query} }}"
        object_fields.append(sub_query)
        object_variables.update(subquery_variables)
    obj_query = " ".join(object_fields)
    return obj_query, object_variables
