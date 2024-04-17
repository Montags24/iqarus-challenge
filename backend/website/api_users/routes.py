import website.api_users.utilities

from flask import request, jsonify
from website import db
from website.api_users import bp
from website.models import User
from werkzeug.security import generate_password_hash


# User CRUD
@bp.route("/", methods=["POST"])
def create_user():
    try:
        api_package = request.get_json()
        new_user_credentials = api_package["new_user_credentials"]
    except KeyError:
        return jsonify(message="Bad api request - please try again"), 400
    except Exception:
        return jsonify(message="An error occured"), 500

    # check if user exists already
    user = website.api_users.utilities.get_user_by_email(new_user_credentials["email"])
    if user is not None:
        return jsonify(message="This email is already in use"), 409

    try:
        # hash password
        new_user_credentials["hashed_password"] = generate_password_hash(
            new_user_credentials["password"]
        )

        # create user and set attributes
        new_user_record = User(
            name=new_user_credentials["name"],
            email=new_user_credentials["email"],
            hashed_password=new_user_credentials["hashed_password"],
        )

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


@bp.route("/")
def test():
    return jsonify({"test": "ok"})
