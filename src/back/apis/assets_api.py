from flask import Blueprint, send_from_directory

assets_api = Blueprint('assets_api', __name__, static_url_path='')


@assets_api.route("/assets/<path:path>")
def assets_get(path):
    print("path: ", path)
    return send_from_directory('src/assets/', path)

