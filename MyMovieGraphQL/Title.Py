from MyMovieGraphQL import GraphQL
from MyMovieGraphQL import attributes
from MyMovieGraphQL import Image, Video
from datetime import date
import re
import requests
import pprint


class Title:
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
        if not re.fullmatch(r"tt\d{7,}", id):
            raise AttributeError(f"The ID must be of form tt____, '{id}' given")
        if not isinstance(allowPrivate, bool):
            raise TypeError(
                f"`allowPrivate` must be of type str, {type(allowPrivate)} given."
            )
        if not isinstance(fetch, bool):
            raise TypeError(f"`allowPrivate` must be of type str, {type(fetch)} given.")
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
                allowPrivate=self.allowPrivate,
            )
            query = f'query {{title(id: "{id}") {{ {sub_query} }}}}'
            query_arg = {"query": query}
            headers = {"Content-Type": "application/json"}
            api_url = "https://api.graphql.imdb.com/"
            r = requests.post(url=api_url, json=query_arg, headers=headers)
            output = r.json()
            errors = output.get("errors")
            data = output.get("data", {}).get("title", {})
        else:
            data = kwargs
        self._data = self._data | self.transorm(data)
        self.id = self._data["id"]

    def transform_key(self, key: str, value) -> dict:
        transformed_dict = {}
        if not value:
            return transformed_dict
        match key:
            case "id":
                transformed_dict["id"] = value
            case "titleText":
                transformed_dict["title"] = value.get("text")
                if value.get("language"):
                    transformed_dict["title language"] = value.get("language").get("id")
                    transformed_dict["title language name"] = value.get("language").get(
                        "text"
                    )
                    transformed_dict["title isOriginal"] = value.get("isOriginalTitle")
            case "originalTitleText":
                transformed_dict["original title"] = value.get("text")
                if value.get("language"):
                    transformed_dict["original title isOriginal"] = value.get(
                        "isOriginalTitle"
                    )
                    transformed_dict["original title language"] = value.get(
                        "language"
                    ).get("id")
                    transformed_dict["original title language name"] = value.get(
                        "language"
                    ).get("text")
            case "releaseYear":
                transformed_dict["releaseYear"] = value.get("year")
            case "releaseDate":
                year = value.get("year")
                month = value.get("month")
                day = value.get("day")
                country = value.get("country")
                if year and month and day:
                    transformed_dict["release date"] = date(year, month, day)
                if country:
                    transformed_dict["release date country"] = country
            case "countriesOfOrigin":
                transformed_dict["countries of origin"] = value.get("countries")
            case "runtime":
                transformed_dict["runtime"] = value.get("seconds")
                transformed_dict["runtime id"] = value.get("id")
                if displayableProperty := value.get("displayableProperty"):
                    if v := displayableProperty.get("value"):
                        transformed_dict["runtime human form"] = v.get("plainText")
                    if language := displayableProperty.get("language"):
                        transformed_dict["runtime language"] = language.get("id")
                        transformed_dict["runtime language name"] = language.get("text")
                    transformed_dict["runtime attributes"] = displayableProperty.get(
                        "attributes"
                    )
                    transformed_dict["runtime country"] = displayableProperty.get(
                        "country"
                    )
            case "productionStatus":
                if currentProductionStage := value.get("currentProductionStage"):
                    transformed_dict["production stage"] = currentProductionStage.get(
                        "text"
                    )
                    transformed_dict["production stage id"] = (
                        currentProductionStage.get("id")
                    )
                if productionStatusHistory := value.get("productionStatusHistory"):
                    transformed_dict["production history"] = [
                        {
                            "date": status.get("date"),
                            "status": status.get("status").get("text"),
                        }
                        for status in productionStatusHistory
                    ]
            case "canHaveEpisodes":
                transformed_dict["can have episodes"] = value
            case "certificate":
                transformed_dict["certificate"] = value.get("rating")
                transformed_dict["certificate country"] = value.get("country")
            case "certificates":
                certificates = []
                if self._data.get("certificate"):
                    certificates.append(
                        {
                            "certificate": self._data.get("certificate"),
                            "certificate country": self._data.get(
                                "certificate country"
                            ),
                        }
                    )
                if nodes := value.get("edges", []):
                    for node in nodes:
                        certificates.append(
                            {
                                "certificate": node.get("node").get("rating"),
                                "certificate country": node.get("node").get("country"),
                            }
                        )
                transformed_dict["certificates"] = certificates

            case "keywords":
                transformed_dict["keywords"] = [
                    kwNode.get("node") for kwNode in value.get("edges")
                ]
            case "genres":
                transformed_dict["genres"] = value.get("genres")
            case "plot":
                if plotText := value.get("plotText"):
                    transformed_dict["plot"] = plotText.get("plainText")
                if language := value.get("language"):
                    transformed_dict["plot language"] = language
            case "plots":
                plots = {}
                if nodes := value.get("edges"):
                    for node in nodes:
                        plot = node.get("node")
                        plotText = plot.get("plotText", {}).get("plainText")
                        plotLanguage = plot.get("language")
                        plotType = plot.get("plotType")
                        if plotType not in plots:
                            plots[plotType] = []
                        plots[plotType].append(
                            {
                                "text": plotText,
                                "language": plotLanguage,
                            }
                        )
                transformed_dict["plots"] = plots
            case "primaryImage":
                transformed_dict["primary image"] = Image.Image(
                    fetch=False, allowPrivate=self.allowPrivate, **value
                )
            case "images":
                if nodes := value.get("edges"):
                    images = []
                    for node in nodes:
                        image_node = node.get("node")
                        images.append(
                            Image.Image(
                                fetch=False,
                                allowPrivate=self.allowPrivate,
                                **image_node,
                            )
                        )
                    transformed_dict["images"] = images
            case "series":
                if value:
                    kwargs = value.get("series")
                    transformed_dict["series"] = Title(
                        fetch=False, allowPrivate=self.allowPrivate, **kwargs
                    )
            case "canRate":
                if value:
                    transformed_dict["can rate"] = value.get("isRatable")
            case "titleType":
                transformed_dict["type"] = value.get("text")
                transformed_dict["type id"] = value.get("id")
                transformed_dict["type language"] = value.get("language")
            case "ratingsSummary":
                transformed_dict["rating"] = value.get("aggregateRating")
                transformed_dict["rating votes"] = value.get("voteCount")
                if topRanking := value.get("topRanking"):
                    transformed_dict["rating top ranking"] = {
                        "id": topRanking.get("id"),
                        "rank": topRanking.get("rank"),
                        "language": topRanking.get("text", {}).get("language"),
                    }
            case "videos":
                if value:
                    transformed_dict["videos total"] = value.get("total")
            case "primaryVideos":
                primaryVideos = []
                if nodes := value.get("edges"):
                    for node in nodes:
                        video_node = node.get("node")
                        primaryVideos.append(
                            Video.Video(
                                fetch=False,
                                allowPrivate=self.allowPrivate,
                                **video_node,
                            )
                        )
                transformed_dict["primary videos"] = primaryVideos
            case "externalLinks":
                externalLinks = []
                if nodes := value.get("edges"):
                    for node in nodes:
                        link_node = node.get("node")
                        externalLinks.append(link_node)
                transformed_dict["external links"] = externalLinks
            case "metacritic":
                metacritic = []
                reviews = value.get("reviews", {})
                if nodes := reviews.get("edges"):
                    for node in nodes:
                        review_node = node.get("node")
                        metacritic.append(review_node)
                transformed_dict["metacritic reviews"] = metacritic
            case "credits":
                credits = []
                if nodes := value.get("edges"):
                    for node in nodes:
                        credit_node = node.get("node")
                        title_dict = credit_node.get("title")
                        name_dict = credit_node.get("name")
                        # TODO Name.Name(...)
                        category_dict = credit_node.get("category", {})
                        title = Title(
                            fetch=False, allowPrivate=self.allowPrivate, **title_dict
                        )
                        credits.append(
                            {
                                "title": title,
                                "name": None,  # TODO
                                "category": category_dict.get("text"),
                                "category": category_dict.get("id"),
                                "language": credit_node.get("language"),
                            }
                        )
                transformed_dict["credits"] = credits
            case "episodeCredits":
                credits = []
                if nodes := value.get("edges"):
                    for node in nodes:
                        credit_node = node.get("node")
                        title_dict = credit_node.get("title")
                        name_dict = credit_node.get("name")
                        # TODO Name.Name(...)
                        creditedRoles = credit_node.get("creditedRoles", {})
                        title = Title(
                            fetch=False, allowPrivate=self.allowPrivate, **title_dict
                        )
                        credits.append(
                            {
                                "title": title,
                                "name": None,  # TODO
                                "roles": creditedRoles,
                            }
                        )
                transformed_dict["episode credits"] = credits
            case "principalCredits":
                principalCredits = {}
                for credit in value:
                    category = credit.get("category", {})
                    credits = []
                    for c in credit.get("credits", []):
                        title_dict = c.get("title")
                        name_dict = c.get("name")
                        title = Title(
                            fetch=False, allowPrivate=self.allowPrivate, **title_dict
                        )
                        credits.append(
                            {
                                "title": title,
                                "name": None,  # TODO
                                "attributes": c.get("attributes"),
                            }
                        )
                    principalCredits[category.get("text")] = {
                        "category": category.get("text"),
                        "category id": category.get("id"),
                        "category language": category.get("language"),
                        "credits": credits,
                    }
                transformed_dict["principal credits"] = principalCredits
            case "principalCreditsV2":
                principalCreditsV2 = {}
                principalCreditsV2_categories = {}
                for credit_section in value:
                    credits = credit_section.get("credits")
                    for credit in credits:
                        title_dict = credit.get("title")
                        title = Title(
                            fetch=False, allowPrivate=self.allowPrivate, **title_dict
                        )
                        name_dict = credit.get("name")
                        if roles := credit.get("creditedRoles", {}).get("edges"):
                            for node in roles:
                                credit_node = node.get("node")
                                credit_category = credit_node.get("category", {}).get(
                                    "text"
                                )
                                credit_text = credit_node.get("text")
                                credit_category_id = credit_node.get(
                                    "category", {}
                                ).get("id")
                                credit_category_language = credit_node.get(
                                    "category", {}
                                ).get("language")
                                if credit_category not in principalCreditsV2:
                                    principalCreditsV2[credit_category] = []
                                principalCreditsV2[credit_category].append(
                                    {
                                        "title": title,
                                        "name": None,  # TODO
                                        "category": credit_category,
                                        "text": credit_text,
                                    }
                                )
                                if credit_category not in principalCreditsV2_categories:
                                    principalCreditsV2_categories[credit_category] = {
                                        "id": credit_category_id,
                                        "language": credit_category_language,
                                    }
                transformed_dict["principal credits v2"] = principalCreditsV2
                transformed_dict["principal credits v2 categories"] = (
                    principalCreditsV2_categories
                )
            case "episodes":
                episodes = []
                episode_nodes = value.get("episodes", {}).get("edges", [])
                for ep in episode_nodes:
                    episode = ep.get("node")
                    title = Title(
                        fetch=False, allowPrivate=self.allowPrivate, **episode
                    )
                    episodes.append(title)
                seasons = value.get("seasons", [])
                seasons = [s.get("number") for s in seasons]
                transformed_dict["season numbers"] = seasons
                transformed_dict["episodes"] = episodes
            case "meterRanking":
                transformed_dict["meter ranking type"] = value.get("meterType")
            case _:
                print(key)
                pprint.pp(value, width=200)
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
            allowPrivate=self.allowPrivate,
            manual=True,
        )
        query = f'query {{title(id: "{self.id}") {{ {sub_query} }}}}'
        query_arg = {"query": query}
        headers = {"Content-Type": "application/json"}
        api_url = "https://api.graphql.imdb.com/"
        r = requests.post(url=api_url, json=query_arg, headers=headers)
        output = r.json()
        errors = output.get("errors")
        data = output.get("data", {}).get("title", {})
        self._data = self._data | self.transorm(data)
        if errors:
            pprint.pp(errors)

