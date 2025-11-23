from MyMovieGraphQL import GraphQL
from MyMovieGraphQL.logger import logger
from MyMovieGraphQL.MyMovie import MyMovie, regex_in
from beartype import beartype

@beartype
def getByID(id: str) -> MyMovie:
    logger.info("Attempting to fetch by ID: %s", id)
    query_name = ""
    args = {
        "id": id,
    }
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
        case r'in\d{7,}':
            query_name = 'interest'
        case r'kw\d{7,}':
            query_name = "keyword"
        case r'ur\d{7,}':
            # Possible without userID, you have to be signed in to get your own data.
            query_name = "userProfile"
            args = {
                "input": {
                    "userId": id,
                },
            }
        case r'ls\d{7,}':
            args = args | {
                "List_items_sort": {
                    "by": "LIST_ORDER",
                    "order": "ASC"
                }
            }
            query_name = "list"
        case r'[A-Za-z_\-0-9]{7,}':
            # XXX: Figure out a better regex, these seem random.
            # "XG6P0TT-NX1o8k_zwliY4A" and "mzERoASQys8" are both poll IDs.
            # Possibly not allow by getByID with the format.
            query_name = 'poll'
        case _:
            raise ValueError(f"Unknown ID format: {id}")
    return GraphQL.search(query_name, **args)
