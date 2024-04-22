import datetime
import jwt
import os
from flask import request, jsonify
from website.auth import bp
from website.models import User
from werkzeug.security import check_password_hash

SESSION_EXPIRES_SECONDS = int(os.environ.get("SESSION_EXPIRES_SECONDS"))
SECRET_KEY = os.environ.get("SECRET_KEY")


# User CRUD
@bp.route("/login", methods=["POST"])
def login():
    try:
        api_package = request.get_json()
    except KeyError:
        return jsonify(message="Bad api request - please try again"), 400
    except Exception:
        return jsonify(message="An error occured"), 500

    try:
        username = api_package["username"]
        password = api_package["password"]

        user = User.query.filter_by(username=username).first()

        if user is None:
            return jsonify(message="User not found"), 404

        correct_password = check_password_hash(user.hashed_password, password)

        if not correct_password:
            return jsonify(message="Incorrect username or password"), 401

        user_dict = user.get_dict()

        # generate jwt for future authentication
        login_time = datetime.datetime.now(tz=datetime.timezone.utc)

        jwt_content = dict(
            exp=login_time + datetime.timedelta(seconds=SESSION_EXPIRES_SECONDS),
            user_id=user_dict["id"],
            username=user_dict["username"],
            logged_on_time_seconds=login_time.timestamp(),
        )

        session_jwt = jwt.encode(jwt_content, SECRET_KEY, algorithm="HS512")

        package = {}
        package["id"] = user_dict["id"]
        package["name"] = user_dict["name"]
        package["username"] = user_dict["username"]
        package["session_jwt"] = session_jwt
        # Add user organisation

        return (
            jsonify(message="Login successful", package=package),
            200,
        )
    except Exception as err:
        print(err)
        return jsonify(message="An error occured during login"), 500
