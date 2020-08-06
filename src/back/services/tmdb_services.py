import requests


def get_cover_path(title):
    """
    Return the cover path of the given movie
    :param title: the title of the movie
    :return: the cover path
    """
    base_url = "https://api.themoviedb.org/3/search/movie?api_key={}&query={}"
    apikey = "4ca2b1ac7501d2a20234b56f7edcfe88"
    url = base_url.format(apikey, title)
    response = requests.get(url)
    cover = response.json()['results'][0]

    return "http://image.tmdb.org/t/p/w500/" + cover['poster_path']
