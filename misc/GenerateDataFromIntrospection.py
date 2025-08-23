import json

with open('introspection.json', 'r') as file:
    data = json.load(file)

sort_by = {}
queries = {}
enums = {}
scalars = {}
inputs = {}
args = {}

for obj, val in data.items():
    if not (val['args'] or val['enumValues'] or val['fields'] or val['inputFields']):
        # Custom scalars like Date, DateTime, URL, etc.
        scalars[obj] = {
            'name': obj,
            'description': val['description'],
        }
    if val['enumValues'] and not (val['args'] or val['fields'] or val['inputFields']):
        enums[obj] = val['enumValues']
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
    if val['inputFields']:
        inputs[obj] = {}
        for input_val in val['inputFields']:
            input_type = input_val['type']
            input_name = input_val['name']
            input_nullable = input_val['nullable']
            input_list = input_val['list']
            input_defaultValue = input_val['defaultValue'] or ''
            inputs[obj][input_name] = {
                'type': input_type,
                'name': input_name,
                'nullable': input_nullable,
                'list': input_list,
                'defaultValue': input_defaultValue,
            }
    for field in val['fields']:
        if field.get('args'):
            if obj not in args:
                args[obj] = {}
            args[obj][field.get('name')] = field.get('args')

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
with open('ENUMS.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(enums, f, indent=2, sort_keys=True)
with open('INPUTS.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(inputs, f, indent=2, sort_keys=True)
with open('SCALARS.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(scalars, f, indent=2, sort_keys=True)
with open('SORT_BY.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(sort_by, f, indent=2, sort_keys=True)
with open('QUERIES.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(queries, f, indent=2, sort_keys=True)
with open('ARGS.json', 'w', encoding="utf-8", newline='\n') as f:
    json.dump(args, f, indent=2, sort_keys=True)