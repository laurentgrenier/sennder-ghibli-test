import requests


def get_movies():
    people = get_people()
    print("people count: ", len(people))
    response = requests.get("https://ghibliapi.herokuapp.com/films")
    movies = response.json()

    for movie in movies:
        movie["characters"] = [character["name"] for character in people if "https://ghibliapi.herokuapp.com/films/" + movie["id"] in character["films"]]

    return movies


def get_people():
    response = requests.get("https://ghibliapi.herokuapp.com/people?fields=name,films&limit=250")
    return response.json()
