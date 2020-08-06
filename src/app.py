# app.py
from flask import Flask
from flask_cors import CORS

from src.back.apis.cover_api import cover_api
from src.back.apis.assets_api import assets_api

from src.front.pages import cache
from src.front.pages import movies_page


def create_app():
    app = Flask(__name__)
    cache.init_app(app)

    app.register_blueprint(assets_api)
    app.register_blueprint(cover_api)
    app.register_blueprint(movies_page)
    CORS(app)
    return app


if __name__ == '__main__':
    create_app().run(port=8000)
