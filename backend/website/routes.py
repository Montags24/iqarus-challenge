import requests
import os
from dotenv import load_dotenv

from flask import current_app as app
from flask import render_template, request, jsonify
from flask_cors import CORS

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

this_directory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(this_directory, "../.env"))


@app.route("/")
@app.route("/index")
def index():
    # This is a vue project that serves the static index file only
    return render_template("index.html")
