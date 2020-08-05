import requests
from src.back.services.omdb_services import OMDB


class Movies:
    list = []

    def load(self):
        response = requests.get("https://ghibliapi.herokuapp.com/films")
        self.list = response.json()

    def get_images(self):
        title = self.list[0]["title"]
        return OMDB.get(title)['Poster']

