import requests


class OMDB:
    @staticmethod
    def get(title):
        base_url = "http://www.omdbapi.com/?t={}&apikey={}"
        omdbapi_key = "dec4d70b"
        url = base_url.format(title, omdbapi_key)
        response = requests.get(url)
        return response.json()
