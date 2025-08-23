from typing import Iterable, Any

class MyMovie:
    def __init__(self, obj: dict) -> None:
        if not isinstance(obj, dict):
            raise TypeError(f"MyMovie's object must be a dict, '{type(obj)}' given.")
        if not obj:
            raise ValueError(f"MyMovie's object dict is empty.")
        self.data: dict[str, Any] = dict()
        self.ofType: str = obj.get('__typename', 'MissingTypeName')
        for k, val in obj.items():
            if not isinstance(k, str):
                raise ValueError(f"Expected all dict keys to be a string, '{k}:{type(k)} = {val}' ")
            # Recursively set the type of each item,
            # making them all a `MyMovie`, a list, or a base type
            key = k.removeprefix(f'{self.ofType}_')
            if key in self.data:
                raise ValueError(f"Key: '{key}', was pased more than once.")
            if isinstance(val, dict):
                self.data[key] = MyMovie(val)
            elif isinstance(val, list):
                self.data[key] = [
                    MyMovie(item) if isinstance(item, dict) else item
                    for item in val
                ]
            else:
                self.data[key] = val
        self.index: int | None = None
        if self.itterableAttribute():
            self.index = 0
    
    def __hash__(self) -> int:
        id = self.data.get('id')
        if not id:
            raise NotImplementedError(f"{self.ofType} is not hashable.")
        # Any that have an ID may be used in a dict/object
        # that requires it to be hashable.
        # Hash on the ID to ensure even partial objects match.
        return hash(id)
    
    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if not isinstance(other, type(self)):
            return False
        if self.ofType != other.ofType:
            return False
        if self.data.get('id') and self.data.get('id') == other.data.get('id'):
            # If the IDs match they are the same.
            return True
        self_pageInfo = self.data.get('pageInfo', {})
        other_pageInfo = other.data.get('pageInfo', {})
        if self_pageInfo and other_pageInfo:
            # Only true when they have the same cursors.
            startCursor = self_pageInfo.get('startCursor') == other_pageInfo.get('startCursor')
            endCursor = self_pageInfo.get('endCursor') == other_pageInfo.get('endCursor')
            return startCursor and endCursor
        keys = set(self.data.keys())
        keys.update(set(other.data.keys()))
        # Loop through all the possible keys and check if they all match
        for key in keys:
            if self.data.get(key) != other.data.get(key):
                return False
        # All keys matched
        return True
    
    def get(self, val):
        return self.data.get(val)
    
    def keys(self):
        return self.data.keys()
    
    def items(self):
        return self.data.items()
    
    def __getitem__(self, val):
        if self.ofType.endswith('Connection') and isinstance(val, int):
            node = self.data.get('edges', [])[val].get('node')
            if len(node.keys()) == 2:
                for k, v in node.items():
                    if k != '__typename':
                        return v
            return node
        return self.data[val] # type: ignore

    def __iter__(self) -> Iterable:
        attr = self.itterableAttribute()
        if attr is None:
            raise TypeError(f"'{self.ofType}' object is not iterable")
        return iter(attr)
    
    def __len__(self) -> int:
        attr = self.itterableAttribute()
        if attr is None:
            raise TypeError(f"'{self.ofType}' object has no len")
        if self.ofType.endswith('Connection'):
            return len(self.data.get('edges', []))
        return 0

    def __next__(self):
        if self.itterableAttribute() is None:
            raise TypeError(f"'{self.ofType}' object is not iterable")
        if self.index is None:
            raise TypeError(f"'{self.ofType}' object has a 'None' index") 
        self.index += 1
        if self.index >= len(self):
            self.index = max(self.index-1, 0)
            raise StopIteration
        value = self.data.get('edges', [])[self.index]
        return value

    def itterableAttribute(self) -> Iterable | None:
        if self.ofType.endswith('Connection'):
            return self.data.get('edges', [])
        return None
