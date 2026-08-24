from MyMovieGraphQL import GraphQL

if __name__ == "__main__":
    with open("GraphQL_generateQuery_Title.snapshot.txt", "w", encoding="utf-8") as file:
        file.write(repr(GraphQL.generateQuery("Title")))
