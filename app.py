# app.py
from flask import Flask
from flask_cors import CORS
from src.back.apis.movies_api import movies_api
from src.views import movies_page

app = Flask(__name__)
app.register_blueprint(movies_api)
app.register_blueprint(movies_page)
CORS(app)

if __name__ == '__main__':
    app.run(port=8000)
