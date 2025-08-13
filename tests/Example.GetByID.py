from MyMovieGraphQL.GetByID import getByID
if __name__ == "__main__":
    # Example usage
    movie_id = "tt1981677" # Pitch Perfect (2012)
    show_id = "tt1553656" #  Under the Dome (2013-2015)
    episode_id = "tt0606035" # House S01E01
    name_id = "nm0908094" # Paul Walker
    name_id2 = "nm0000206" # Keanu Reeves
    
    movie_data = getByID(movie_id)
    print(movie_data)

    show_data = getByID(show_id)
    print(show_data)
    
    name_data = getByID(name_id)
    print(name_data)

    name_data2 = getByID(name_id2)
    print(name_data2)

    episode_data = getByID(episode_id)
    try:
        print(f"{episode_data.series} - {episode_data}") # type: ignore
    except AttributeError:
        print(episode_data)
