from flask import request, jsonify
from website import db
from website.api_users import bp
from website.models import User
from werkzeug.security import generate_password_hash
from website.api_users.utilities import validate_user


# User CRUD
@bp.route("/", methods=["POST"])
def create_user():
    try:
        api_package = request.get_json()
    except KeyError:
        return jsonify(message="Bad api request - please try again"), 400
    except Exception:
        return jsonify(message="An error occured"), 500

    # check if user exists already
    user = User.query.filter_by(username=api_package["username"]).first()
    if user is not None:
        return jsonify(message="This username is already in use"), 409

    try:
        api_package["hashed_password"] = generate_password_hash(api_package["password"])

        # create user and set attributes
        new_user_record = User()
        for name, value in api_package.items():
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
        return jsonify(message="An error occured creating a user"), 500


@bp.route("/", methods=["PUT"])
@validate_user
def edit_user(**kwargs):
    try:
        api_package = request.get_json()
        edited_name = api_package["edited_name"]
    except KeyError:
        return jsonify(message="Bad api request - please try again"), 400
    except Exception:
        return jsonify(message="An error occured"), 500

    # get user from database using values from decoded JWT
    user = User.query.filter_by(
        username=kwargs["username"], id=kwargs["user_id"]
    ).first()

    try:
        # set new name
        setattr(user, "name", edited_name)
        db.session.commit()

        user_dict = user.get_dict()

        return (
            jsonify(message="The user was successfully created.", user=user_dict),
            201,
        )
    except Exception as err:
        print(err)
        db.session.rollback()
        db.session.flush()  # for resetting non-commited .add()
        return jsonify(message="Error updating user details"), 500
