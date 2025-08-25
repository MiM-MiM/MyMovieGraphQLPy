from typing import Iterable, Any
import re
from dataclasses import dataclass
from . import GraphQL

@dataclass
class regex_in:
    string: str

    def __eq__(self, other: str | re.Pattern):  # type: ignore
        if isinstance(other, str):
            other = re.compile(other)
        assert isinstance(other, re.Pattern)
        return other.fullmatch(self.string) is not None

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
    
    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"{type(other)} cannot be added to {type(self)}.")
        if self.ofType != other.ofType:
            raise TypeError(f"{other.ofType} cannot be added to {self.ofType}.")
        for k, v  in other.items():
            if k not in self.data:
                self.data[k] = v
                continue
            # Need to merge
            self_val = self.data.get(k)
            if self_val is None:
                self.data[k] = v
                continue
            if isinstance(v, type(self)) and isinstance(self_val, type(self)):
                if v.ofType != self_val.ofType:
                    raise TypeError(f'{v.ofType} and {self_val.ofType} are not the same.')
                if v.ofType.endswith('Connection'):
                    # replace the non-node objects and append the two edges
                    v_pageInfo = v.data.get('pageInfo', {})
                    v_endCursor = v_pageInfo.get('endCursor')
                    v_startCursor = v_pageInfo.get('startCursor')
                    v_hasNextPage = v_pageInfo.get('hasNextPage')
                    self_pageInfo = self_val.data.get('pageInfo', {})
                    self_endCursor = self_pageInfo.get('endCursor')
                    self_startCursor = self_pageInfo.get('startCursor')
                    if v_startCursor == self_startCursor and v_endCursor == self_endCursor:
                        # The cursors match, no new data was fetched
                        continue
                    # Update the pageInfo to the new data.
                    self.data[k]['pageInfo']['endCursor'] = v_endCursor
                    self.data[k]['pageInfo']['startCursor'] = v_startCursor
                    self.data[k]['pageInfo']['hasNextPage'] = v_hasNextPage
                    if self.data[k]['edges'] is not None:
                        if v.data['edges'] is not None:
                            # XXX: Changed to appending, may switch back to pre-pending upon feedback.
                            self.data[k]['edges'].extend(v.data['edges'])
                            continue
                        self.data[k]['edges'] = self.data[k]['edges']
        return self

        
    def update(self,
               attribute: str | list = "",
               previous: bool = False,
               variables: dict = {},
    ):
        """ Update the object and return the updated values.
        Args:
           attribute(str | list): The attribute to be updated,
                if not provided the base object must be a connection.
            variables(dict): The variables to be used for running the update.
        """
        # Sanity check
        GraphQL.load_config_json()
        search: str = self.ofType.removesuffix("Connection")
        noUpdate = []
        # Search is always the type with the first letter lowercase.
        if len(search) > 1:
            # Should always be longer than 1
            search = search[0].lower() + search[1:]
        foundQuery = False
        for query in GraphQL.DATA['Query']["fields"]:
            if query["name"] == search:
                foundQuery = True
        if not foundQuery:
            raise AttributeError(f"'{self.ofType}' does not support being updated. Please update from the main object.")
        if not attribute:
            # This is to be only used for searches
            # or connections that have a search of the same name.
            pageInfo = self.data.get('pageInfo', {})
            endCursor = pageInfo.get('endCursor')
            startCursor = pageInfo.get('startCursor')
            if previous and startCursor is not None and "before" not in variables:
                variables["before"] = startCursor
            elif not previous and endCursor is not None and "after" not in variables:
                variables["after"] = endCursor
            if not previous and not pageInfo.get('hasNextPage'):
                # There is no next page
                return None
        elif self.data.get('id') is not None:
            variables['id'] = self.data.get('id')
            if isinstance(attribute, str):
                currentAttributes = [attribute]
            else:
                currentAttributes = attribute
            for attrib in currentAttributes:
                currentData = self.data.get(attrib)
                if currentData is not None:
                    if isinstance(currentData, type(self)):
                        if currentData.ofType.endswith('Connection'):
                            pageInfo = currentData.get('pageInfo', {})
                            hasNextPage = pageInfo.get('hasNextPage')
                            # startCursor is the first node, endCursor is the last node.
                            # Updating the next page we use the end.
                            endCursor = pageInfo.get('endCursor')
                            after = f"{self.ofType}_{attrib}_after"
                            if not hasNextPage:
                                # Nothing to update, remove the attribute.
                                # Calling for the items after the last cursor
                                # will result in an error.
                                noUpdate.append(attrib)
                                continue
                            variables[after] = endCursor
        for attrib in noUpdate:
            if isinstance(attribute, str):
                attribute = []
            else:
                attribute.remove(attrib)
        if attribute == []:
            # There is nothing to update
            return None
        update = GraphQL.search(searchName=search, limitAttributes=attribute, **variables)
        if not isinstance(update, type(self)) or update is None:
            raise ValueError(f"Updating {self.ofType} failed...")
        self += update
        return update
    
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
    
    def get(self, val, default: Any = None):
        return self.data.get(val, default)
    
    def keys(self):
        return self.data.keys()
    
    def items(self):
        return self.data.items()
    
    def __repr__(self) -> str:
        id = self.get('id')
        if id is not None:
            return f"<--- {self.ofType} ({id}): {self.__str__()} --->"
        return self.__str__()
    
    def __str__(self) -> str:
        match regex_in(self.ofType):
            case 'Title':
                return self._titleStr()
            case 'Name':
                return self._nameStr()
            case 'YearRange':
                return self._yearRangeStr()
            case 'TitleGenre':
                return self._titleGenreStr()
            case 'Certificate':
                return self._certificateStr()
            case 'RatingsSummary':
                return self._ratingsSummaryStr()
            case r'.*Connection':
                # Any connections we can return the string form of the list
                return str(list(self.itterableAttribute()))
            case _:
                return self._otherStr()

    def _certificateStr(self) -> str:
        rating = self.data.get('rating')
        country = self.data.get('country')
        if rating is not None and country is not None:
            return f"{rating} ({country})"
        if rating is not None:
            return str(rating)
        return 'Unknown Rating'

    def _connection(self) -> str:
        attr = self.itterableAttribute()
        if isinstance(attr, Iterable):
            return str(list(attr))
        return self.ofType

    def _nameStr(self) -> str:
        name = self.data.get('nameText')
        birthDate = self.data.get('birthDate')
        deathDate = self.data.get('deathDate')
        deathStatus = self.data.get('deathStatus')
        birthStr, deathStr = "", ""
        if birthDate is not None:
            birthStr = str(birthDate['date'])
        if deathDate is not None:
            deathStr = str(deathDate['date'])
        nameString = str(name)
        if deathStatus == 'ALIVE':
            nameString = f"{name} ({birthStr})"
        if deathStatus in ["DEAD", "PRESUMED_DEAD"]:
            nameString = f"{name} ({birthStr} - {deathStr})"
        return nameString

    def _titleGenreStr(self):
        genre = self.data.get('genre')
        if isinstance(genre, type(self)):
            genre = str(genre)
        elif genre is None:
            genre = ''
        return genre
    
    def _ratingsSummaryStr(self) -> str:
        aggregateRating = self.get('aggregateRating')
        voteCount = self.get('voteCount')
        aggregateRatingStr = 'Unknown'
        if aggregateRating is not None:
            aggregateRatingStr = f"{aggregateRating}/10"
        if voteCount is not None:
            aggregateRatingStr = f"{aggregateRatingStr} ({voteCount} votes)"
        return aggregateRatingStr

    def _yearRangeStr(self):
        year: int | None = self.data.get('year', 0)
        endYear: int | None = self.data.get('endYear', 0)
        yearRangeStr: str = ""
        if year:
            yearRangeStr = f"{year}"
        if endYear:
            yearRangeStr = f"{yearRangeStr}-{endYear}"
        return yearRangeStr

    def _titleStr(self) -> str:
        title = self.data.get('titleText')
        year = self.data.get('releaseYear')
        return f"{title} ({year})"

    def _otherStr(self):
        text = self.data.get('text')
        url = self.data.get('url')
        value = self.data.get('value')
        plainText = self.data.get('plainText')
        displayableProperty = self.data.get('displayableProperty')
        if text is not None:
            return str(text)
        if url is not None:
            return str(url)
        if plainText is not None and isinstance(plainText, str):
            return plainText
        if value is not None:
            return str(value)
        current = ''
        # Any that we want to us starts/ends/contains should go here.
        for key in self.data.keys():
            if self.data.get(key) is None:
                continue
            if key.startswith('current'):
                current = str(self.data[key])
            if key == 'language' and 'Language' in self.ofType:
                return str(self.data.get('language'))
        if current:
            return current
        if displayableProperty is not None:
            return str(displayableProperty)
        keys = [
            key
            for key in self.data.keys()
            if not key.startswith('_')
        ]
        # Types with a single attribute should print that.
        if len(keys) == 1:
            return str(self.data.get(keys[0]))
        return f"<--- {self.ofType}: {keys} --->"

    def __getitem__(self, index):
        if self.ofType.endswith('Connection') and isinstance(index, int):
            node = self.data.get('edges', [])[index].get('node')
            if len(node.keys()) == 2:
                for k, v in node.items():
                    if k != '__typename':
                        return v
            return node
        return self.data[index] # type: ignore
    
    def __setitem__(self, index , val):
        if not isinstance(index, str):
            raise TypeError("Index must be a string.")
        self.data[index] = val

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
            edges = [
                edge.get('node')
                for edge in self.data.get('edges', [])
            ]
            return iter(edges)

        return None
