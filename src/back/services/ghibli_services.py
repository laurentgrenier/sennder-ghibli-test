import requests
from src.back.services.tmdb_services import get_cover_path


def get_movies():
    """
    Get the list of all Studio Ghibli movies with cover and characters
    :return: the list of movies
    """
    # get the characters of the movie
    people = get_people()

    # get the movies
    response = requests.get("https://ghibliapi.herokuapp.com/films")
    movies = response.json()

    for movie in movies:
        # set the character of the movie
        movie["characters"] = [character["name"] for character in people if "https://ghibliapi.herokuapp.com/films/" +
                               movie["id"] in character["films"]]
        # set the cover of the movie
        movie["cover"] = get_cover_path(movie["title"])
    return movies


def get_people():
    """
    Retrieve all the characters of the movies
    :return: a list of characters
    """
    response = requests.get("https://ghibliapi.herokuapp.com/people?fields=name,films&limit=250")
    return response.json()
