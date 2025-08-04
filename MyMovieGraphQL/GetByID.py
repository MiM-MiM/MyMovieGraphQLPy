import re
import requests
from dataclasses import dataclass

from MyMovieGraphQL import GraphQL, attributes
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
    match regex_in(id):
        case r'tt\d{7,}':
            # Movie ID
            obj = getTitleByID(id)
        case r'nm\d{7,}':
            # Name ID
            obj = getNameByID(id)
        case _:
            raise ValueError(f"Unknown ID format: {id}")
    return obj

def getTitleByID(id: str) -> Title:
    # fmt: off
    title_possible = attributes.Title
    query_keys = [
        "id", "titleText", "titleType", "originalTitleText", "releaseYear",
        "releaseDate", "countriesOfOrigin", "runtime", "productionStatus",
        "canHaveEpisodes", "certificate", "primaryImage", "series",
        "keywords", "genres", "plot"
    ]
    # fmt: on
    sub_query = GraphQL.query_builder(
        data=title_possible,
        keys=query_keys,
        allowPrivate=False,
    )
    query = f'query {{title(id: "{id}") {{ {sub_query} }}}}'
    query_arg = {"query": query}
    r = requests.post(url=API_URL, json=query_arg, headers=HEADERS)
    data = r.json().get("data", {}).get("title", {})
    return Title(**data)

def getNameByID(id: str) -> Name:
    title_possible = attributes.NameLimited
    sub_query = GraphQL.query_builder(
        data=title_possible,
        keys=list(title_possible.keys()),
        allowPrivate=False,
    )
    query = f'query {{name(id: "{id}") {{ {sub_query} }}}}'
    query_arg = {"query": query}
    r = requests.post(url=API_URL, json=query_arg, headers=HEADERS)
    data = r.json().get("data", {}).get("name", {})
    return Name(**data)
