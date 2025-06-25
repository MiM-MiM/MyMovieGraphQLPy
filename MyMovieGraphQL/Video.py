from MyMovieGraphQL import GraphQL
from MyMovieGraphQL import attributes
from datetime import date
import re
import requests


class Video:
    def __init__(self, **kwargs):
        id = kwargs.get("id")
        allowPrivate = kwargs.get("allowPrivate", False)
        fetch = kwargs.get("allowPrivate", True)
        try:
            del kwargs["fetch"]
        except KeyError:
            pass
        try:
            del kwargs["allowPrivate"]
        except KeyError:
            pass
        if not isinstance(id, str):
            raise TypeError(f"`id` must be of type str, {type(id)} given.")
        if not re.fullmatch(r"vi\d{7,}", id):
            raise AttributeError(f"The ID must be of form vi____, '{id}' given")
        if not isinstance(allowPrivate, bool):
            raise TypeError(
                f"`allowPrivate` must be of type str, {type(allowPrivate)} given."
            )
        if not isinstance(fetch, bool):
            raise TypeError(f"`allowPrivate` must be of type str, {type(fetch)} given.")
        self._data = {}
        self.allowPrivate = allowPrivate
        if fetch:
            video_possible = attributes.Video
            self._possible_keys = list(video_possible.keys())
            # fmt: off
            query_keys = ["id", "name"]
            # fmt: on
            sub_query = GraphQL.query_builder(
                data=video_possible,
                keys=query_keys,
                allowPrivate=self.allowPrivate,
            )
            query = f'query {{video(id: "{id}") {{ {sub_query} }}}}'
            query_arg = {"query": query}
            headers = {"Content-Type": "application/json"}
            api_url = "https://api.graphql.imdb.com/"
            r = requests.post(url=api_url, json=query_arg, headers=headers)
            output = r.json()
            errors = output.get("errors")
            data = output.get("data", {}).get("image", {})
        else:
            data = kwargs
        self._data = self._data | self.transorm(data)
        self.id = self._data["id"]

    def transorm(self, response: dict) -> dict:
        transformed_dict = {}
        for key in response.keys():
            value = response[key]
            key_dict = self.transform_key(key, value)
            transformed_dict = transformed_dict | key_dict
        return transformed_dict

    def transform_key(self, key: str, value) -> dict:
        transformed_dict = {}
        if not value:
            return transformed_dict
        match key:
            case "id":
                transformed_dict["id"] = value
            case "name":
                if value.get("language"):
                    transformed_dict["language"] = value.get("language")
                if value.get("value"):
                    transformed_dict["type"] = value.get("value")
        return transformed_dict
