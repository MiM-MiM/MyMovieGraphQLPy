from MyMovieGraphQL import GraphQL, attributes
import requests
import importlib.resources as resources
import json

API_URL = "https://api.graphql.imdb.com/"
HEADERS = {"Content-Type": "application/json"}

# TODO: Implement these types.
MISSING_TYPES = ['TitleTrackRecommendationsConnection', 'TitleChartRankingsConnection', 'ExportDetailConnection', 'NameTrackRecommendationsConnection', 'ChartNameSearchConnection', 'ReviewsConnection', 'TrendingTitleConnection', 'VideoRecommendationsConnection', 'RatingsConnection', 'RecentlyViewedConnection', 'SuggestionSearchConnection', 'MainSearchConnection', 'PollsConnection', 'ListCollectionConnection', 'EmailPreferences', 'ShowtimesTitleConnection', 'SavedSearchFiltersConnection', 'FollowedEntitiesConnection', 'NameChartRankingsConnection', 'TrendingNameConnection', 'TopGrossingReleasesConnection', 'TrackedNamesConnection', 'TopPicksConnection', 'WebAdsOutput', 'ChartTitleSearchConnection', 'InvalidAuthProviderInterstitialOutput', 'WebAdsConfigOutput', 'FanPicksConnection', 'WatchedTitlesConnection', 'TrackedTitlesConnection', 'TrendingVideoConnection']
MISSING_QUERIES = ['fanPicksTitles', 'professionNameTrackRecommendations', 'savedSearchFilters', 'showtimesTitlesByCinemas', 'topGrossingReleases', 'lists', 'userVotedPolls', 'webAdsConfig', 'titleChartRankings', 'trackedNames', 'chartNames', 'emailPreferences', 'professionTitleTrackRecommendations', 'polls', 'userRatings', 'similarNameTrackRecommendations', 'userListSearch', 'userReviews', 'trackedTitles', 'showtimesTitles', 'topPicksTitles', 'chartTitles', 'followedEntities', 'topListsForItem', 'topTrendingSetsPredefined', 'nameChartRankings', 'suggestionSearch', 'mainSearch', 'topTrendingVideos', 'topTrendingNames', 'getExports', 'topTrendingTitles', 'webAds', 'userWatchedTitles', 'invalidAuthProviderInterstitial', 'unreleasedTitleTrackRecommendations', 'recentlyViewedItems', 'similarTitleTrackRecommendations', 'videoRecommendations']


ENUMS, INPUTS, QUERIES, SCALARS, SORT_BY = {}, {}, {}, {}, {}
def load_config_json():
    global ENUMS, INPUTS, QUERIES, SCALARS, SORT_BY
    # Only load it once
    if not (ENUMS and INPUTS and QUERIES and SCALARS and SORT_BY):
        with resources.open_text('MyMovieGraphQL.data', 'ENUMS.json') as f:
            ENUMS = json.load(f)
        with resources.open_text('MyMovieGraphQL.data', 'INPUTS.json') as f:
            INPUTS = json.load(f)
        with resources.open_text('MyMovieGraphQL.data', 'QUERIES.json') as f:
            QUERIES = json.load(f)
        with resources.open_text('MyMovieGraphQL.data', 'SCALARS.json') as f:
            SCALARS = json.load(f)
        with resources.open_text('MyMovieGraphQL.data', 'SORT_BY.json') as f:
            SORT_BY = json.load(f)

def generate_argument_dict(name: str):
    # Ensure the config files are loaded.
    load_config_json()
    if name not in QUERIES:
        raise ValueError(f"Query, '{name}', was not found.")
    if name in MISSING_QUERIES:
        raise NotImplementedError(f"Query, '{name}', is not yet implemented.")
    query = QUERIES[name]
    args = query['args']
    arg_dict = {}
    base_types = ['String', 'Int', 'Float', 'ID', 'Boolean']
    def recursive_get_types(type_dict: dict):
        arg_type_dict = {}
        for k, v in type_dict.items():
            v_type = v['type']
            if v_type in base_types or v_type in SCALARS or v_type in ENUMS:
                arg_type_dict[k] = None
                continue
            arg_type_dict[k] = recursive_get_types(INPUTS[v_type])
        return arg_type_dict
    for arg in args:
        isRequired = not arg['nullable']
        defaultValue = arg['defaultValue']
        arg_type = arg['type']
        if defaultValue:
            arg_dict[arg['name']] = defaultValue
        elif arg_type in base_types or arg_type in SCALARS or arg_type in ENUMS:
            arg_dict[arg['name']] = None
        elif arg_type in INPUTS:
            arg_dict[arg['name']] = recursive_get_types(INPUTS[arg_type])
        else:
            raise NotImplementedError(f"Type, `{arg_type}`, is not implemented, please report.")
    return arg_dict


def generate_input_args(query: dict):
    input_variables_types = []
    input_variables = []
    for arg in query['args']:
        arg_name = arg['name']
        arg_type = arg['type']
        arg_type_str = f"{arg_type}"
        if arg['list'] and not arg['nullable']:
            arg_type_str = f"[{arg_type}!]!"
        elif arg['list'] and arg['nullable']:
            arg_type_str = f"[{arg_type}]"
        elif not arg['list'] and not arg['nullable']:
            arg_type_str = f"{arg_type}!"
        elif not arg['list'] and arg['nullable']:
            arg_type_str = f"{arg_type}"
        input_variables_types.append(f"${arg_name}: {arg_type_str}")
        input_variables.append(f"{arg_name}: ${arg_name}")
    if input_variables and input_variables_types:
        return (
            f"({', '.join(input_variables_types)})",
            f"({', '.join(input_variables)})"
        )
    return "", ""

def generate_query(name: str = 'title'):
    # Ensure the config files are loaded.
    load_config_json()
    if name not in QUERIES:
        raise ValueError(f"Query, '{name}', was not found.")
    if name in MISSING_QUERIES:
        raise NotImplementedError(f"Query, '{name}', is not yet implemented.")
    sub_query = ""
    query = QUERIES[name]
    input_variables_types, input_variables = generate_input_args(query)
    output_type = query['output']
    static_types = ['Boolean', 'String', 'Int', 'Float', 'ID'] + list(ENUMS.keys()) + list(SCALARS.keys())
    if output_type in static_types:
        sub_query = f" {output_type} "
    else:
        match output_type:
            # Cases we should limit
            case 'Title':
                output_type = "TitleLimited"
            case 'Name':
                output_type = "NameLimited"
            # Connection types for searches.
            case "AdvancedNameSearchConnection":
                output_type = "AdvancedNameSearchResult"
            case "AdvancedTitleSearchConnection":
                output_type = "AdvancedTitleSearchResult"
        output_type = output_type.replace("Connection", "").removesuffix("Search")
        # Ensure the main object is used for the data, keep keys of limited version.
        possible_data = getattr(attributes, output_type.removesuffix('Limited'))
        possible_data_keys = list(getattr(attributes, output_type).keys())
        if output_type in ['Title', 'TitleLimited'] and 'series' not in possible_data_keys:
            possible_data_keys.append('series')
        sub_query = GraphQL.query_builder(
            data=possible_data,
            keys=possible_data_keys,
            allowPrivate=False,
        )
    if query['output'].endswith("Connection"):
        # Connections should get the pagnation.
        pageInfo_data = attributes.PageInfo
        pageInfo_data_keys = list(pageInfo_data.keys())
        pageInfo_sub_query = GraphQL.query_builder(
            data=pageInfo_data,
            keys=pageInfo_data_keys,
            allowPrivate=False,
        )
        page_info = f"total pageInfo {{ {pageInfo_sub_query} }}"
        sub_query = f"edges {{ node {{ {sub_query} }} }} {page_info}"
    query_string = f"query {name}{input_variables_types} {{ {name}{input_variables} {{ {sub_query} }} }}"
    return query_string

def query(name: str, variables: dict, as_dict: bool = False) -> object | dict:
    query_arg = {"query": generate_query(name), "variables": variables}
    r = requests.post(url=API_URL, json=query_arg, headers=HEADERS).json()
    errors = r.get('errors')
    if errors:
        print(errors)
        error_messages = f'\n'.join([str(e) for e in errors])
        raise ValueError(f"Query failed to execute ({len(errors)} errors):\n{'-'*40}\n{error_messages}\n{'-'*40}")
    if as_dict:
        return r['data'][name]
    # TODO: Create the actual object.
    raise NotImplementedError("Object generation is not yet completed, use as_dict=True")
