from MyMovieGraphQL import GraphQL
from MyMovieGraphQL import attributes
from datetime import date
import re
import requests
import pprint


class Title:
    def __init__(self, **kwargs):
        id = kwargs.get('id')
        allowPrivate = kwargs.get('allowPrivate', False)
        fetch = kwargs.get('allowPrivate', True)
        if not isinstance(id, str):
            raise TypeError(f"`id` must be of type str, {type(id)} given.")
        if not re.fullmatch(r"tt\d{7,}", id):
            raise AttributeError(f"The ID must be of form tt____, '{id}' given")
        if not isinstance(allowPrivate, bool):
            raise TypeError(
                f"`allowPrivate` must be of type str, {type(allowPrivate)} given."
            )
        if not isinstance(fetch, bool):
            raise TypeError(
                f"`allowPrivate` must be of type str, {type(fetch)} given."
            )
        self._data = {}
        self.allowPrivate = allowPrivate
        if fetch:
            title_possible = attributes.Title
            self._possible_keys = list(title_possible.keys())
            # fmt: off
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
                allowSub=True,
                allowPrivate=self.allowPrivate,
            )
            query = f'query {{title(id: "{id}") {{ {sub_query} }}}}'
            query_arg = {"query": query}
            headers = {"Content-Type": "application/json"}
            api_url = "https://api.graphql.imdb.com/"
            r = requests.post(url=api_url, json=query_arg, headers=headers)
            output = r.json()
            errors = output.get('errors')
            data = output.get('data', {}).get('title', {})
        else:
            data = kwargs
        self._data = self._data | self.transorm(data)
        self.id = self._data['id']
    def transform_key(self, key: str, value) -> dict:
        transformed_dict = {}
        match key:
            case "id":
                transformed_dict['id'] = value
            case 'titleText':
                transformed_dict['title'] = value.get('text')
                if value.get('language'):
                    transformed_dict['title language'] = value.get('language').get('id')
                    transformed_dict['title language name'] = value.get('language').get('text')
                    transformed_dict['title isOriginal'] = value.get('isOriginalTitle')
            case 'originalTitleText':
                transformed_dict['original title'] = value.get('text')
                if value.get('language'):
                    transformed_dict['original title isOriginal'] = value.get('isOriginalTitle')
                    transformed_dict['original title language'] = value.get('language').get('id')
                    transformed_dict['original title language name'] = value.get('language').get('text')
            case 'releaseYear':
                transformed_dict['releaseYear'] = value.get('year')
            case 'releaseDate':
                year = value.get('year')
                month = value.get('month')
                day = value.get('day')
                country = value.get('country')
                if year and month and day:
                    transformed_dict["release date"] = date(year, month, day)
                if country:
                    transformed_dict["release date country"] = country
            case 'countriesOfOrigin':
                transformed_dict["countries of origin"] = value.get('countries')
            case 'runtime':
                transformed_dict["runtime"] = value.get('seconds')
                transformed_dict["runtime id"] = value.get('id')
                if displayableProperty := value.get('displayableProperty'):
                    if v := displayableProperty.get('value'):
                        transformed_dict["runtime human form"] = v.get('plainText')
                    if language := displayableProperty.get('language'):
                        transformed_dict["runtime language"] = language.get('id')
                        transformed_dict["runtime language name"] = language.get('text')
                    transformed_dict["runtime attributes"] = displayableProperty.get('attributes')
                    transformed_dict["runtime country"] = displayableProperty.get('country')
            case 'productionStatus':
                if currentProductionStage := value.get('currentProductionStage'):
                    transformed_dict["production stage"]  = currentProductionStage.get('text')
                    transformed_dict["production stage id"]  = currentProductionStage.get('id')
                if productionStatusHistory := value.get('productionStatusHistory'):
                    transformed_dict["production history"]  = [
                        {
                            'date': status.get('date'),
                            'status': status.get('status').get('text')
                        }
                        for status in productionStatusHistory
                    ]
            case 'canHaveEpisodes':
                transformed_dict["can have episodes"] = value
            case 'certificate':
                transformed_dict["certificate"] = value.get('rating')
                transformed_dict["certificate country"] = value.get('rating')
            case 'keywords':
                transformed_dict['keywords'] = [
                    kwNode.get('node')
                    for kwNode in value.get('edges')
                ]
            case 'genres':
                transformed_dict['genres'] = value.get('genres')
            case 'plot':
                if plotText := value.get('plotText'):
                    transformed_dict['plot'] = plotText.get('plainText')
                if language := value.get('language'):
                    transformed_dict['plot language'] = language
            case 'primaryImage':
                transformed_dict['primary image id'] = value.get('id')
                transformed_dict['primary image type'] = value.get('type')
                transformed_dict['primary image width'] = value.get('width')
                transformed_dict['primary image height'] = value.get('height')
                transformed_dict['primary image'] = value.get('url')
                transformed_dict['primary image languages'] = value.get('languages')
                # TODO parse with Names()
                #transformed_dict['primary image names'] = value.get('names')
                #pprint.pp(value)
                #exit()
            case 'series':
                if value:
                    kwargs = value.get('series')
                    transformed_dict['series'] = Title(fetch=False, **kwargs)
            case 'canRate':
                if value:
                    transformed_dict['can rate'] = value.get('isRatable')
            case 'titleType':
                transformed_dict['type'] = value.get('text')
                transformed_dict['type id'] = value.get('id')
                transformed_dict['type language'] = value.get('language')
            case _:
                print(key)
                print(value)
                exit()
        return transformed_dict
    def transorm(self, response: dict) -> dict:
        transformed_dict = {}
        for key in response.keys():
            value = response[key]
            key_dict = self.transform_key(key, value)
            transformed_dict = transformed_dict | key_dict
        return transformed_dict
    def update(self, key: str | list, paramersts: dict = {}):
        if not isinstance(key, list) and not isinstance(key, str):
            raise TypeError(f"The key(s) must be a string or list, {type(key)} given.")
        if isinstance(key, str):
            keys = [key]
        else:
            keys = key
        if not any([isinstance(k, str) for k in keys]):
            raise TypeError("The keys must be strings")
        if not isinstance(paramersts, dict):
            raise TypeError(f"The `paramersts` must be a dict, {paramersts} given.")
        sub_query = GraphQL.query_builder(
            data=attributes.Title,
            keys=keys,
            allowSub=True,
            allowPrivate=self.allowPrivate,
        )
        query = f'query {{title(id: "{self.id}") {{ {sub_query} }}}}'
        query_arg = {"query": query}
        headers = {"Content-Type": "application/json"}
        api_url = "https://api.graphql.imdb.com/"
        r = requests.post(url=api_url, json=query_arg, headers=headers)
        output = r.json()
        errors = output.get('errors')
        data = output.get('data', {}).get('title', {})
        self._data = self._data | self.transorm(data)
        


if __name__ == "__main__":
    test = Title(id='tt0636289')
    print(test._data.get('can rate'))
    test.update('canRate')
    print(test._data.get('can rate'))
