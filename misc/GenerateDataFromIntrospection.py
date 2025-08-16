import json

with open('introspection.json', 'r') as file:
    data = json.load(file)

constraints = {}
sort_by = {}
sorts = {}
queries = {}
enums = {}
scalars = {}

for obj, val in data.items():
    if not (val['args'] or val['enumValues'] or val['fields'] or val['inputFields']):
        # Custom scalars like Date, DateTime, URL, etc.
        scalars[obj] = {
            'name': obj,
            'description': val['description'],
        }
    if val['enumValues'] and not (val['args'] or val['fields'] or val['inputFields']):
        enums[obj] = val['enumValues']
    if obj.endswith('Constraints') or obj.endswith('Constraint'):
        constraints[obj] = {}
        for constraint in val['inputFields']:
            constraint_type = constraint['type']
            constraint_name = constraint['name']
            constraint_nullable = constraint['nullable']
            constraint_list = constraint['list']
            constraint_defaultValue = constraint['defaultValue'] or ''
            constraints[obj][constraint_name] = {
                'type': constraint_type,
                'name': constraint_name,
                'nullable': constraint_nullable,
                'list': constraint_list,
                'defaultValue': constraint_defaultValue,
            }
    if obj.endswith('SortBy'):
        sort_by[obj] = {}
        # These are ENUMs
        for sort_by_val in val['enumValues']:
            sort_by_description = sort_by_val['description']
            sort_by_name = sort_by_val['name']
            sort_by[obj][sort_by_name] = {
                'description': sort_by_description,
                'name': sort_by_name,
            }
    if obj.endswith('Sort'):
        sorts[obj] = {}
        for sort in val['inputFields']:
            sort_type = sort['type']
            sort_name = sort['name']
            sort_nullable = sort['nullable']
            sort_list = sort['list']
            sort_defaultValue = sort['defaultValue'] or ''
            sorts[obj][sort_name] = {
                'type': sort_type,
                'name': sort_name,
                'nullable': sort_nullable,
                'list': sort_list,
                'defaultValue': sort_defaultValue,
            }

for query in data['Query']['fields']:
    query_name = query['name']
    query_output = query['type']
    query_output_list = query['list']  # If it is a list, it will return a list
    query_output_nullable = query['nullable']  # If it is nullable, a query may not return anything.
    query_description = query['description']
    query_args = query['args'] or []  # args with nullable = False are required.
    if query_name and query_output:
        queries[query_name] = {
            'name': query_name,
            'description': query_description,
            'output': query_output,
            'list': query_output_list,
            'nullable': query_output_nullable,
            'args': query_args,
        }

# Dump the data to json files.
with open('CONSTRAINTS.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(constraints, f, indent=2, sort_keys=True)
with open('ENUMS.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(enums, f, indent=2, sort_keys=True)
with open('SCALARS.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(scalars, f, indent=2, sort_keys=True)
with open('SORT_BY.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(sort_by, f, indent=2, sort_keys=True)
with open('SORTS.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(sorts, f, indent=2, sort_keys=True)
with open('QUERIES.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(queries, f, indent=2, sort_keys=True)