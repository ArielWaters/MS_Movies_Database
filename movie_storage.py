import json
import requests


def list_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    try:
        with open("movies.json", "r") as file:
            movies_data = json.load(file)
    except FileNotFoundError:
        movies_data = {}

    return movies_data


def add_movie(name):
    """
    Adds a movie to the movies database.
    Fetches the movie information from the OMDb API based on the title,
    and saves it to the data structure.
    """

    try:
        # Make a request to the OMDb API
        url = f"http://www.omdbapi.com/?t={name}&apikey=efa33e0b"
        response = requests.get(url)
        data = response.json()

        # Extract the reqired paramteres from the API response
        if data["Response"] == "True":
            movie_data = {
                "name": data["Title"],
                "year": data["Year"],
                "rating": data["imdbRating"],
                "poster": data["Poster"]
            }

            # Save the movie data to the movies data structure
            movies_data = list_movies()
            movies_data[name] = movie_data
            save_movies(movies_data)
            print(f"Movie '{name}' successfully added!")
        else:
            print(f"Failed to fetch movie '{name}' from the OMDb API.")

    except requests.exceptions.RequestException as e:
        print("Failed to connect to the OMDb API. Please check your internet connection.")


def delete_movie(name):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies_data = list_movies()
    if name in movies_data:
        del movies_data[name]
        save_movies(movies_data)


def update_movie(name, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies_data = list_movies()
    if name in movies_data:
        movies_data[name]["rating"] = rating
        save_movies(movies_data)


def save_movies(movies_data):
    """Helper function to save movies to the JSON file"""
    with open("movies.json", "w") as file:
        json.dump(movies_data, file, indent=4)


def generate_website():
    """
    Generates the website based on the template and movie data.
    Creates an HTML file called index.html with the full website content.
    """
    template_file = "index_template.html"
    output_file = "index.html"

    movies_data = list_movies()

    with open(template_file, "r") as file:
        template = file.read()

    movie_grid = ""
    for name, movie in movies_data.items():
        output = f"<div class='movie'>"
        output += f"<img class='movie-poster' src='{movie['poster']}' alt='{movie['name']}'>"
        output += f"<div class='movie-details'>"
        output += f"<div class='movie-name'>{movie['name']}</div>"
        output += f"<div class='movie-year'>{movie['year']}</div>"
        output += "</div></div>"
        movie_grid += output

    website_content = template.replace("__TEMPLATE_TITLE__", "My Movie App")
    website_content = website_content.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)

    with open(output_file, "w") as file:
        file.write(website_content)

    print("Website was generated successfully.")
