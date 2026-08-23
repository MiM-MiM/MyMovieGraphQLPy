import json

with open('INTROSPECTION.json', 'r', encoding='utf-8') as file:
    DATA = json.load(file)

MAIN = """# API Overview
The following documentation is unofficial. Anything listed in the API files here may change.
See [IMDb Developer](https://developer.imdb.com/documentation/api-documentation/) for the official documentation.

# Endpoints
- Realtime: https://api.graphql.imdb.com/
- Cached: https://caching.graphql.imdb.com/

# Base information
- Brackets, `[ ]`, indicate list
- Exclamation, `!`, indicates non-null
- Supports alias names
- Fragment notation is `... on Type { field1 field2 }`
- Custom Scalars are strings, see the respective description for the format.
- Variables can be used in queries

# Headers
These headers can be set to alter the responses. Many responses are not impacted by these being present or not.
- `x-amzn-customer-id`
- `x-amzn-sessionid`
- `x-amzn-transitive-authentication-token`
- `x-auth-session-customer-id`
- `x-coordinate`
- `x-imdb-adsystem-overrides`
- `x-imdb-client-ip`
- `x-imdb-client-name`
- `x-imdb-client-version`
- `x-imdb-consent-info`
- `x-imdb-customer-id`
- `x-imdb-detected-country`
- `x-imdb-detected-country-region`
- `x-imdb-detected-time-zone`
- `x-imdb-internal-client`
- `x-imdb-non-1p-client`
- `x-imdb-normalized-languages`
- `x-imdb-user-country`
- `x-imdb-user-language`

# Query
These are able to be called against the above endpoints.
"""

SECTIONS = {
    "SCALAR": "# Builtin GraphQL Scalars\n- Boolean\n- Float\n- Int\n- String\n- ID\n\n# Custom Scalars\nIMDb defined scalars, strings of a specific format.",
    "ENUM": "# Enums\nStrings, case sensitive. Used for filtering or indicating data types/sources.",
    "OBJECT": "# Objects\nThese may have fields, arguments, or a collection of other types. If they have `possible types` they require the fragment notation to select non-overlapping fields. If field names overlap and the types are different, you must specify an alias to select both.",
    "FILTER": "# Filters\nThese are used solely for the purpose of filtering selections.",
    "CONSTRAINT": "# Constraints\nSimilar to filters, generally more complex filtering abilities.",
    "CONNECTION": "# Connections and Edges\nThese are essentially lists of other objects that are paginated.",
    "SORT": "# Sort\nThese are used to specify the sort objects.",
    "EXPERIMENTAL": "# Experimental\nThese generally should not be used, see descriptions."
}

def get_target_category(name: str, kind: str = ""):
    """Consistently resolves target file category and base anchor."""
    if not kind and name in DATA:
        kind = DATA[name].get('kind', '')
        
    if kind == "ENUM":
        return "API-ENUM", "enums", "ENUM"
    elif kind == "SCALAR":
        return "API-Scalar", "builtin-graphql-scalars", "SCALAR"
    elif kind == "INPUT_OBJECT" or name.endswith("Filter"):
        return "API-Object-Filter", "filters", "FILTER"
    elif name.endswith("Constraint"):
        return "API-Object-Constraint", "constraints", "CONSTRAINT"
    elif name.endswith(("Connection", "Edge", "Node", "PageInfo")):
        return "API-Object-Connection", "connections-and-edges", "CONNECTION"
    elif name.endswith(("Sort", "SortBy")):
        return "API-Object-Sort", "sort", "SORT"
    elif "Experimental" in name:
        return "API-Object-Experimental", "experimental", "EXPERIMENTAL"
    else:
        return "API-Object", "objects", "OBJECT"

def clean_type_name(t: str) -> str:
    return t.replace('[', '').replace(']', '').replace('!', '').replace('\\', '').strip()

def nameToLink(raw_type: str, display_text: str):
    clean_name = clean_type_name(raw_type)
    if clean_name in DATA:
        target_file, _, _ = get_target_category(clean_name, DATA[clean_name].get('kind'))
        return f"[{display_text}]({target_file}#{clean_name.lower()})"
    return f"[{display_text}](API-Scalar#builtin-graphql-scalars)"

def format_description(desc: str) -> str:
    if not desc:
        return ""
    desc = desc.strip().replace("@", r"\@").replace('[', r'\[').replace(']', r'\]')
    return f"> {desc}".replace('\n', '\n> ')

def argsToString(args: list = [], name: str = ""):
    if not args:
        return name
    arg_strings = []
    for arg in args or []:
        arg_name = arg['name']
        base_type = arg["type"]
        nullable = arg.get('nullable', True)
        isList = arg.get('list', False)
        
        # Build raw display representation
        if isList and not nullable:
            formatted_type = f"[{base_type}!]!"
        elif isList:
            formatted_type = f"[{base_type}]"
        elif not nullable:
            formatted_type = f"{base_type}!"
        else:
            formatted_type = f"{base_type}"
            
        linked_type = nameToLink(base_type, formatted_type.replace('[', r'\[').replace(']', r'\]'))
        arg_strings.append(f"{arg_name}: {linked_type}")
    return f"{name}({', '.join(arg_strings)})"

# 1. Process Queries
for query in DATA.get('Query', {}).get("fields", []):
    name = query.get("name", "")
    output = query.get("type", "")
    description = format_description(query.get("description", ""))
    args = argsToString(query.get('args', []), name)
    
    if "\\[ID!\\]!" in args or "\\[ID\\]" in args:
        output = f"[{output}]"
        
    output_link = nameToLink(query.get("type", ""), f"`{output}`")
    MAIN += f"\n### {args}\n\nReturns: {output_link}\n"
    if description:
        MAIN += f"\n{description}\n"

# 2. Process Types
for t, v in DATA.items():
    if t == "Query":
        continue
        
    name = v.get("name", "")
    kind = v.get('kind', "")
    description = format_description(v.get("description", ""))
    fields = v.get('fields') or []
    enumValues = v.get("enumValues") or []
    possibleTypes = v.get("possibleTypes") or []
    input_fields = v.get('inputFields') or []
    
    target_file, top_anchor, section_key = get_target_category(name, kind)
    
    block = f"\n\n## {name}"
    if description:
        block += f"\n\n{description}"
        
    if kind == "ENUM":
        if enumValues:
            enums = '\n- '.join([enum['name'] for enum in enumValues])
            block += f"\n- {enums}"
    elif kind == "SCALAR":
        pass  # Header & description already added
    else:
        if input_fields:
            args_str = argsToString(input_fields, name)
            block += f"\n\n- {args_str}"
            
        if fields:
            block += "\n\n### Fields"
            for field in fields:
                f_name = field["name"]
                f_type = field["type"]
                f_nullable = field.get("nullable", True)
                f_list = field.get("list", False)
                f_desc = format_description(field.get("description", ""))
                
                if not f_nullable and f_list:
                    type_str = f"[{f_type}!]!"
                elif f_nullable and f_list:
                    type_str = f"[{f_type}]"
                elif not f_nullable:
                    type_str = f"{f_type}!"
                else:
                    type_str = f"{f_type}"
                    
                field_link = nameToLink(f_type, f"`{type_str}`")
                block += f"\n- {f_name}: {field_link}"
                if f_desc:
                    block += f"\n{f_desc}"
                    
        if possibleTypes:
            pt_links = [nameToLink(pt, f"`{pt}`") for pt in possibleTypes]
            block += f"\n\n### Possible Types\n- " + "\n- ".join(pt_links)
            
    block += f"\n\n[Return to Top](#{top_anchor})\n"
    SECTIONS[section_key] += block

# 3. Write Wiki Files
output_paths = {
    'API Overview.md': MAIN,
    'API-ENUM.md': SECTIONS["ENUM"] + "\n",
    'API-Scalar.md': SECTIONS["SCALAR"] + "\n",
    'API-Object.md': SECTIONS["OBJECT"] + "\n",
    'API-Object-Filter.md': SECTIONS["FILTER"] + "\n",
    'API-Object-Constraint.md': SECTIONS["CONSTRAINT"] + "\n",
    'API-Object-Connection.md': SECTIONS["CONNECTION"] + "\n",
    'API-Object-Sort.md': SECTIONS["SORT"] + "\n",
    'API-Object-Experimental.md': SECTIONS["EXPERIMENTAL"] + "\n",
}

for filename, content in output_paths.items():
    with open(f'../../../MyMovieGraphQLPy.wiki/{filename}', 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
