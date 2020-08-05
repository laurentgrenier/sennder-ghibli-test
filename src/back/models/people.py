import requests


class People:
    list = []

    def load(self):
        response = requests.get("https://ghibliapi.herokuapp.com/people")
        self.list = response.json()
