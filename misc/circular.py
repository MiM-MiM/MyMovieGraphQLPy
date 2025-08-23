import json, copy
from collections import deque
with open('INTROSPECTION.json', 'r') as file:
    DATA = json.load(file)


"""A few pre-defined limited types, rest will be generated.
Generation is done by using a BFS search to see if we hit a
cycle back at the starting point.
Once a cycle is hit we create a LIMITED version of it.
This version will test each attribute to see if it leads
to a cycle again, if none detected, the argument stays.
Repeated for every type and save the result in `LIMITED.json`
"""
LIMITED = {
    "Title": [
        "id", "canonicalUrl", "titleType",
        "releaseYear", "titleText", "originalTitleText",
    ],
    "Name": [
        "id", "canonicalUrl", "bio",
        "akas", "birthDate", "nameText",
        "birthLocation", "birthName", "death",
        "deathCause", "deathDate", "deathLocation",
        "deathStatus", "height",
    ],
    "Cinema": [
        "id", "accessibility", "contactDetails",
        "location", "name",
    ],
    "Company": [
        "id", "bio", "companyText",
        "companyTypes", "country", "acronyms",
    ],
    "News": [
        "id", "articleTitle", "byline",
        "date", "externalUrl", "image",
        "language", "source", "text",
    ],
    "Image": [
        "id", "type", "width"
        "height", "url", "languages",
    ],
    "Interest": [
        "id", "category", "description"
        "engagementStatistics", "primaryImage", "primaryText",
        "score", "secondaryText", "visibilityLevel",
    ],
    "Video": [
        "id", "contentType", "createdDate",
        "description", "runtime",
    ],
}



def bfs(start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        neighbors = copy.deepcopy(DATA[current_node]['fields'])
        if current_node in LIMITED:
            neighbors = [i for i in neighbors if i["name"] in LIMITED[current_node]]
        neighbors += DATA[current_node]['possibleTypes']
        for neighbor in neighbors:
            if isinstance(neighbor, str):
                neighbor_type = neighbor
            else:
                neighbor_type = neighbor["type"]
            if neighbor_type == start_node:
                return True
            if neighbor_type not in DATA:
                continue
            if neighbor_type not in visited:
                visited.add(neighbor_type)
                queue.append(neighbor_type)
    return False
for check_type in DATA:
    if bfs(check_type):
        check_type_names = [
            field['name']
            for field in DATA[check_type]['fields']
        ]
        LIMITED[check_type] = LIMITED.get(check_type, [])
        for name in check_type_names:
            LIMITED[check_type].append(name)
            if bfs(check_type):
                LIMITED[check_type].remove(name)

for check_type in DATA:
    if bfs(check_type):
        print(f"{check_type} is the start of a cycle still")
with open('LIMITED.json', 'w') as f:
    json.dump(LIMITED, f, indent=2, sort_keys=True)