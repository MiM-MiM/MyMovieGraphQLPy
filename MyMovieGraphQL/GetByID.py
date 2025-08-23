import re
from dataclasses import dataclass

from MyMovieGraphQL import GraphQL, MyMovie

@dataclass
class regex_in:
    string: str

    def __eq__(self, other: str | re.Pattern):  # type: ignore
        if isinstance(other, str):
            other = re.compile(other)
        assert isinstance(other, re.Pattern)
        return other.fullmatch(self.string) is not None

def getByID(id: str) -> object:
    query_name = ""
    match regex_in(id):
        case r'tt\d{7,}':
            query_name = "title"
        case r'nm\d{7,}':
            query_name = "name"
        case r'ci\d{7,}':
            query_name = "cinema"
        case r'co\d{7,}':
            query_name = "company"
        case 'creditCategory':
            query_name = "creditCategory"
            raise NotImplemented("creditCategory is not yet implemented, unknown ID format.")
        case r'rm\d{7,}':
            query_name = "image"
        case r'imageGallery':
            query_name = "imageGallery"
            raise NotImplemented("imageGallery is not yet implemented, unknown ID format.")
        case r'interest':
            query_name = 'interest'
            raise NotImplemented("interest is not yet implemented, unknown ID format.")
        case r'kw\d{7,}':
            query_name = "keyword"
        case r'ls\d{7,}':
            query_name = "list"
        case _:
            raise ValueError(f"Unknown ID format: {id}")
    return MyMovie(GraphQL.search(query_name, id=id))
