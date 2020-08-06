import requests


def get_movies():
    """
    Get the list of all Studio Ghibli movies with cover and characters
    :return: the list of movies
    """
    # get the characters of the movie
    people = get_people()

    # get the films
    movies = get_films()

    for movie in movies:
        # set the character of the movie
        movie["characters"] = [character["name"] for character in people if "https://ghibliapi.herokuapp.com/films/" +
                               movie["id"] in character["films"]]
    return movies


def get_films():
    """
    Retrieve all films from the Ghibli films API
    :return: a list of films
    """
    response = requests.get("https://ghibliapi.herokuapp.com/films?fields=id,title,release_date")
    return response.json()


def get_people():
    """
    Retrieve all the characters of the movies
    :return: a list of characters
    """
    response = requests.get("https://ghibliapi.herokuapp.com/people?fields=name,films&limit=250")
    return response.json()
