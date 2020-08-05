# app.py
from flask import Flask
from flask_cors import CORS

from src.back.apis.assets_api import assets_api

from src.views import cache
from src.views import movies_page

app = Flask(__name__)
cache.init_app(app)

app.register_blueprint(assets_api)
app.register_blueprint(movies_page)
CORS(app)

if __name__ == '__main__':
    app.run(port=8000)
