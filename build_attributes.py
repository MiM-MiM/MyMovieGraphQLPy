from MyMovieGraphQL import attributes
# TODO: Fix why it creates two VideoConnection classes.

classes = dict()

def edge_class(edge_name: str) -> str:
    edge_name = edge_name.replace("Limited", "")
    edge_name_new = edge_name.removesuffix("Connection")
    # Handle pluralization for specific edge names
    if edge_name_new in ['NameBios', 'Certificates',
                         "CreditedWithNames", "ImageTypes",
                         "NameRelations", "PollAnswers",
                         "Polls", "ProductionDates",
                         "Reviews", "SharedTitles"]:
        edge_name_new = edge_name_new.removesuffix("s")
    if edge_name_new in ['ContributorRankings']:
        edge_name_new = edge_name_new.removesuffix("ings")
    return f"""
class {edge_name}(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {{type(node)}}")
            self.edges.append({edge_name_new}(**node.get("node", {{}})))
"""
all_edge_classes = set()

for k in dir(attributes):
    if k.startswith("_"):
        continue
    if 'Limited' in k:
        continue
    if not hasattr(attributes, k):
        continue
    if not isinstance(getattr(attributes, k), dict):
        continue
    edge_classes = []
    equal_items = []
    has_id = False
    class_str = f"class {k}:\n"
    class_str += "    def __init__(self, **kwargs):\n"
    if len(getattr(attributes, k).values()) == 0:
        class_str += "        pass\n"
    for key, value in getattr(attributes, k).items():
        if key == "id":
            has_id = True
        if key in ['from', 'to']:
            key = f"{key}_date"
        if key.startswith("*"):
            key = key[1:]
        equal_items.append(f"self.{key} == other.{key}")
        if isinstance(value, str):
            class_str += f"""        if kwargs.get('{key}'):
            self.{key} = {value.replace('Limited', '')}(**kwargs.get('{key}', {{}}))
        else:
            self.{key} = None
"""
            if value.endswith("Connection") and value not in all_edge_classes:
                classes[value] = edge_class(value)
                edge_classes.append(edge_class(value))
                all_edge_classes.add(value)
        else:
            val = value()
            if val == '':
                val = '""'
            class_str += f"        self.{key} = kwargs.get('{key}', {val})\n"
        """
        try:
            with open(f"Attributes/{k}.py", "w") as file:
                    file.write(class_str)
        except IOError as e:
            print(f"Error writing to file: {e}")
        """
    class_str += "    def __eq__(self, other):\n"
    class_str += f"        if not isinstance(other, {k}):\n"
    class_str += "            return False\n"
    if has_id:
        class_str += "        return self.id == other.id\n"
    else:
        if not equal_items:
            class_str += f"        return True\n"
        else:
            class_str += f"        return ({' and '.join(equal_items)})\n"
    classes[k] = class_str
    #print(class_str)
    #print("\n\n".join(edge_classes))

print("""class Edge:
    def __init__(self, **kwargs):
        self.pageInfo = kwargs.get("PageInfo", {})
        self.edges = kwargs.get("edges", [])
""")
class_names = sorted(classes.keys())

for name in class_names:
    print(classes[name])
