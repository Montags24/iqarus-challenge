import requests
import utilities
import os
from dotenv import load_dotenv

from flask import current_app as app
from flask import render_template, request, jsonify
from flask_cors import CORS
from website import db
from website.models import User
from werkzeug.security import generate_password_hash


# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

this_directory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(this_directory, "../.env"))


@app.route("/")
@app.route("/index")
def index():
    # This is a vue project that serves the static index file only
    return render_template("index.html")


# User CRUD
@app.route("/api/user/create", methods=["POST"])
def create_user():
    try:
        api_package = request.get_json()
        new_user_credentials = api_package["new_user_credentials"]
    except KeyError:
        return jsonify(message="Bad api request - please try again"), 400
    except Exception:
        return jsonify(message="An error occured"), 500

    # check if user exists already
    user = utilities.get_user_by_email(new_user_credentials["email"])
    if user is not None:
        return jsonify(message="This email is already in use"), 409

    try:
        # hash password
        new_user_credentials["hashed_password"] = generate_password_hash(
            new_user_credentials["hashed_password"]
        )

        # create user and set attributes
        new_user_record = User()
        for name, value in new_user_credentials.items():
            if hasattr(new_user_record, name):
                setattr(new_user_record, name, value)
        db.session.add(new_user_record)
        db.session.commit()
        user_dict = new_user_record.get_dict()

        return (
            jsonify(message="The user was successfully created.", new_user=user_dict),
            201,
        )
    except Exception as err:
        print(err)
        db.session.rollback()
        db.session.flush()  # for resetting non-commited .add()
        return jsonify(message="The user was not added"), 500
