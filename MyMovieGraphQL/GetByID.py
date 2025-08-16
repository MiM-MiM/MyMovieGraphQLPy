import re
import requests
from dataclasses import dataclass

from MyMovieGraphQL.Query import query
from MyMovieGraphQL.Classes import Title, Name

API_URL = "https://api.graphql.imdb.com/"
HEADERS = {"Content-Type": "application/json"}

@dataclass
class regex_in:
    string: str

    def __eq__(self, other: str | re.Pattern):  # type: ignore
        if isinstance(other, str):
            other = re.compile(other)
        assert isinstance(other, re.Pattern)
        return other.fullmatch(self.string) is not None

def getByID(id: str) -> object:
    obj = None
    # TODO: Change the case to not use the dict type and use the object generated. Requires `Query.py` update.
    match regex_in(id):
        case r'tt\d{7,}':
            # Movie ID
            data = query('title', {'id': id}, True)
            obj = Title(**data)
        case r'nm\d{7,}':
            # Name ID
            data = query('name', {'id': id}, True)
            obj = Name(**data)
        case _:
            raise ValueError(f"Unknown ID format: {id}")
    return obj
