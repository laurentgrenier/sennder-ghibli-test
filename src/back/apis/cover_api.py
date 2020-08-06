from flask import Blueprint, jsonify
from src.back.services.tmdb_services import get_cover_path

cover_api = Blueprint('cover_api', __name__)


@cover_api.route("/cover/<string:title>")
def cover_get(title):
    """
    Retrieve the cover image of the give movie
    :param title: the title of the movie
    :return: a json representing the title and the path toward the cover image
    """
    return jsonify({
        'title': title,
        'path': get_cover_path(title)
    })

