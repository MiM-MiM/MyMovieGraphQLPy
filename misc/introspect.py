
import requests
import re
import time
import pprint
import json


# Rate limiting settings
RATE_LIMIT_DELAY = 0.5  # 0.5 seconds between API calls
introspection = {}
found_types = 0

def clean_name(name: str):
    chars_to_remove = "[]!"
    pattern = '[' + re.escape(''.join(chars_to_remove)) + ']'
    return re.sub(pattern, '', name)

def get_type(obj: dict):
    arg_type = obj.get("type", {}).get('name')
    if not arg_type:
        arg_type = obj.get("type", {}).get('ofType').get('name')
    if not arg_type:
        arg_type = obj.get("type", {}).get('ofType').get('ofType').get('name')
    if not arg_type:
        arg_type = obj.get("type", {}).get('ofType').get('ofType').get('ofType').get('name')
    return clean_name(arg_type)
def get_isList(obj: dict):
    try:
        isList = obj.get("type", {}).get('kind') == 'LIST'
        if not isList:
            isList = obj.get("type", {}).get('ofType').get('kind') == 'LIST'
        if not isList:
            isList = obj.get("type", {}).get('ofType').get('ofType').get('kind') == 'LIST'
        if not isList:
            isList = obj.get("type", {}).get('ofType').get('ofType').get('ofType').get('kind') == 'LIST'
    except AttributeError:
        isList = False
    return isList

def get_nulable(obj: dict):
    try:
        not_null = obj.get("type", {}).get('kind') == 'NON_NULL'
        if not not_null:
            isList = obj.get("type", {}).get('ofType').get('kind') == 'NON_NULL'
        if not not_null:
            isList = obj.get("type", {}).get('ofType').get('ofType').get('kind') == 'NON_NULL'
        if not not_null:
            isList = obj.get("type", {}).get('ofType').get('ofType').get('ofType').get('kind') == 'NON_NULL'
    except AttributeError:
        not_null = False
    return not not_null

def introspect(name: str = 'Query'):
    global introspection, found_types
    if name.startswith('__') or name in ['String', 'Int', 'Float', 'Boolean', 'ID', 'Scalar']:
        # Skip base types, allow introspection of custom types to get descriptions.
        return
    if name in introspection:
        # Skip already done ones.
        return
    if name != "Query":
        # Do one every 0.5s to avoid rate limits.
        time.sleep(RATE_LIMIT_DELAY)
    found_types += 1
    print(f"Introspecting #{found_types}: {name}")
    HEADERS = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    API = "https://api.graphql.imdb.com/"
    # XXX: Can clean up and move to dynamic generating of the query, allowing dynamic nesting.
    QUERY = {
        "variables": {"name": name},
        "query": f"""
        query type($name: String!) {{
            introspect: __type(name: $name) {{
                name
                description
                kind
                enumValues {{
                    name
                    description
                }}
                fields {{
                    name
                    description
                    type {{
                        name
                        kind
                        ofType {{
                            name
                            kind
                            ofType {{
                                name
                                kind
                                ofType {{
                                    name
                                    kind
                                }}
                            }}
                        }}
                    }}
                    args {{
                        name
                        description
                        type {{
                            name
                            kind
                            ofType {{
                                name
                                kind
                                ofType {{
                                    name
                                    kind
                                    ofType {{
                                        name
                                        kind
                                    }}
                                }}
                            }}
                        }}
                        defaultValue
                    }}
                }}
                inputFields {{
                    name
                    description
                    type {{
                        name
                        kind
                        ofType {{
                            name
                            kind
                            ofType {{
                                name
                                kind
                                ofType {{
                                    name
                                    kind
                                    ofType {{
                                        name
                                        kind
                                    }}
                                }}
                            }}
                        }}
                    }}
                    defaultValue
                }}
            }}
        }}
        """
    }
    # Possible new types
    possible_new_types = set()
    r = requests.post(url=API, json=QUERY, headers=HEADERS).json()
    introspect_data = r['data']['introspect']

    enumValues = introspect_data.get('enumValues') or []
    inputFields = introspect_data.get('inputFields') or []
    description = introspect_data.get('description') or []
    args = introspect_data.get('args') or []
    fields = introspect_data.get('fields') or []
    args_compact = []
    inputFields_compact = []
    fields_compact = []

    # XXX: Can be cleaned up and moved to a function.
    for field in fields:
        field_name = field.get('name') or ''
        field_type = get_type(field)
        if field_type not in introspection:
            possible_new_types.add(field_type)
        field_isList = get_isList(field)
        field_nullable = get_nulable(field)
        field_description = field.get('description') or ''
        field_args = field.get('args') or []
        field_args_compact = []
        for arg in field_args:
            field_arg_name = arg.get('name') or ''
            field_arg_type = get_type(arg)
            if field_arg_type not in introspection:
                possible_new_types.add(field_arg_type)
            field_arg_isList = get_isList(arg)
            field_arg_nullable = get_nulable(arg)
            field_arg_description = arg.get('description') or ''
            field_arg_defaultValue = arg.get('defaultValue') or ''
            field_args_compact.append({
                'name': field_arg_name,
                'type': field_arg_type,
                'list': field_arg_isList,
                'nullable': field_arg_nullable,
                'description': field_arg_description,
                "defaultValue": field_arg_defaultValue,
            })
        fields_compact.append({
            'name': field_name,
            'type': field_type,
            'list': field_isList,
            'nullable': field_nullable,
            'args': field_args_compact,
            'description': field_description,
        })
    for field in inputFields:
        field_name = field.get('name') or ''
        field_type = get_type(field)
        if field_type not in introspection:
            possible_new_types.add(field_type)
        field_isList = get_isList(field)
        field_nullable = get_nulable(field)
        field_description = field.get('description') or ''
        field_args = field.get('args') or []
        field_args_compact = []
        field_defaultValue = field.get('defaultValue') or ''
        inputFields_compact.append({
            'name': field_name,
            'type': field_type,
            'list': field_isList,
            'nullable': field_nullable,
            'args': field_args_compact,
            'description': field_description,
            'defaultValue': field_defaultValue,
        })
    introspection[name] = {
        'name': name,
        'enumValues': enumValues,
        'inputFields': inputFields_compact,
        'args': args_compact,
        'fields': fields_compact,
        'description': description,
    }
    for obj in possible_new_types:
        introspect(obj)
    
if __name__ == "__main__":
    introspect()
    with open('introspection.json', 'w') as f:
        json.dump(introspection, f, indent=2, sort_keys=True)
