from MyMovieGraphQL import GraphQL, MyMovie, regex_in

def getByID(id: str) -> MyMovie:
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
