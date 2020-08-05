from flask import Blueprint, request
from src.back.helpers.apis_helpers import CustomError, DecimalEncoder
import json
import requests

movies_api = Blueprint('movies_api', __name__)


@movies_api.route("/back/movies")
def movies_get():
    try:
        response = requests.get("https://ghibliapi.herokuapp.com/films")
    except:
        return CustomError("GET ALL", 400).throw()
    else:
        return json.dumps(response.json(), indent=4, cls=DecimalEncoder)
