from flask import render_template
from flask import Blueprint
from src.back.services.ghibli_services import get_movies
from flask_caching import Cache

movies_page = Blueprint('movies_page', __name__, template_folder="templates")
cache = Cache(config={'CACHE_TYPE': 'simple'})


@movies_page.route("/movies")
@cache.cached(timeout=60)
def movies_page_get():
    movies = get_movies()
    return render_template("movies.html", movies=movies, base_url="http://localhost:8000/")

