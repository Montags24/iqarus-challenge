import os
from dotenv import load_dotenv
from flask import current_app as app
from flask import render_template

this_directory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(this_directory, "../.env"))


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def index():
    # This is a vue project that serves the static index file only
    return render_template("index.html")
