#!/usr/bin/python3
"""app module"""

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def flask_isnt_fun(chester):
    """handles teardown_appcontext"""
    storage.close()


@app.errorhandler(404)
def page_not_found(err):
    """handles page not found"""
    return make_response(jsonify(error="Not found"), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST")
    if (host is None):
        host = '0.0.0.0'
    port = getenv("HBNB_API_PORT")
    if (port is None):
        port = '5000'
    app.run(host, port, threaded=True)
