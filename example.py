#!/usr/bin/env python3
"""
Example script demonstrating how to use the MyMovieGraphQL module
to fetch and display movie information from IMDb.
"""

# Import the Title class from the MyMovieGraphQL module
from MyMovieGraphQL.Title import Title
import sys


def safe_get(data_dict, key, default="Not available"):
    """Safely get a value from a dictionary, returning a default if not found"""
    if data_dict is None:
        return default
    return data_dict.get(key, default)


def main():
    try:
        # Create a Title instance with an IMDb ID
        # The ID format should be "tt" followed by 7+ digits
        # This example uses "The Shawshank Redemption" (tt0111161)
        print("Fetching information for 'The Shawshank Redemption'...")
        movie = Title(id='tt0111161')

        # The data retrieved from IMDb is stored in the _data dictionary
        # Let's print some basic information about the movie

        print("\n=== Basic Movie Information ===")
        print(f"Title: {safe_get(movie._data, 'title')}")
        print(f"Release Year: {safe_get(movie._data, 'releaseYear')}")
        print(f"Type: {safe_get(movie._data, 'type')}")

        # Get additional information like runtime, countries of origin, etc.
        print("\n=== Additional Details ===")
        if 'runtime' in movie._data and movie._data.get('runtime') is not None:
            try:
                # Convert seconds to minutes for better readability
                runtime_minutes = movie._data.get('runtime') // 60
                print(f"Runtime: {runtime_minutes} minutes")
            except (TypeError, ValueError) as e:
                print(f"Runtime: Error calculating runtime - {e}")
        else:
            print("Runtime: Not available")

        # Print countries of origin if available
        if 'countries of origin' in movie._data and movie._data.get('countries of origin'):
            try:
                countries = movie._data.get('countries of origin')
                country_names = [c.get('text', 'Unknown') for c in countries if c]
                print(f"Countries of Origin: {', '.join(country_names)}")
            except Exception as e:
                print(f"Countries of Origin: Error retrieving countries - {e}")
        else:
            print("Countries of Origin: Not available")

        # Print the plot if available
        if 'plot' in movie._data and movie._data.get('plot'):
            print("\n=== Plot ===")
            print(safe_get(movie._data, 'plot'))
        else:
            print("\n=== Plot ===")
            print("Plot: Not available")

        # The update method can be used to fetch additional information
        # For example, let's get the certificate rating
        print("\n=== Updating with Additional Information ===")
        try:
            movie.update('certificate')
            print(f"Certificate: {safe_get(movie._data, 'certificate')}")
        except Exception as e:
            print(f"Certificate: Error retrieving certificate - {e}")

        # You can also fetch multiple attributes at once
        try:
            movie.update(['genres', 'canRate'])

            # Print genres if available
            if 'genres' in movie._data and movie._data.get('genres'):
                try:
                    # Handle genres based on the actual data structure
                    # From the error, we know it's a list and not a dictionary
                    genres = movie._data.get('genres')
                    if isinstance(genres, list):
                        genre_texts = [g.get('text', 'Unknown') for g in genres if g]
                        print(f"Genres: {', '.join(genre_texts)}")
                    else:
                        # If it's a dictionary (as in attributes.py structure), try to get genres field
                        genre_list = getattr(genres, 'genres', [])
                        genre_texts = [g.get('text', 'Unknown') for g in genre_list if g]
                        print(f"Genres: {', '.join(genre_texts)}")
                except Exception as e:
                    print(f"Genres: Error processing genres - {e}")
            else:
                print("Genres: Not available")

            # Print whether the movie can be rated
            print(f"Can Rate: {safe_get(movie._data, 'can rate')}")
        except Exception as e:
            print(f"Error updating additional attributes: {e}")

        # You can also fetch information for a TV show
        # Let's try with "Breaking Bad" (tt0903747)
        print("\n\n=== TV Show Example: Breaking Bad ===")
        try:
            tv_show = Title(id='tt0903747')

            print(f"Title: {safe_get(tv_show._data, 'title')}")
            print(f"Type: {safe_get(tv_show._data, 'type')}")
            print(f"Release Year: {safe_get(tv_show._data, 'releaseYear')}")

            # Check if it can have episodes (should be True for TV shows)
            print(f"Can Have Episodes: {safe_get(tv_show._data, 'can have episodes')}")
        except Exception as e:
            print(f"Error fetching TV show information: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

if __name__ == "__main__":
    main()
