from flask import render_template
from flask import Blueprint
from src.back.services.ghibli_services import get_movies

movies_page = Blueprint('movies_page', __name__, template_folder="templates")


@movies_page.route("/movies")
def movies_page_get():
    movies = get_movies()

    # print(movies.get_images())
    return render_template("index.html", movies=movies)

