import jwt
import datetime
from flask import request, jsonify
from flask import current_app as app
from functools import wraps


def is_jwt_valid(exp_time: str) -> bool:
    try:
        current_time = datetime.datetime.now(tz=datetime.timezone.utc).timestamp()

        # Check if the token is not expired
        if current_time <= exp_time:
            return True
        else:
            return False
    except Exception as err:
        print(err)
        return False


def decode_jwt(user_jwt: str):
    decoded_token = jwt.decode(user_jwt, app.secret_key, algorithms=["HS512"])
    exp_time = decoded_token.get("exp", 0)
    user_id = decoded_token.get("user_id", 0)
    username = decoded_token.get("username", 0)

    return exp_time, user_id, username


def validate_user(route_function):
    """
    Decorator for validating JSON Web Tokens (JWT) in the Authorization header of incoming requests.

    The decorator extracts the JWT from the Authorization header, decodes it to retrieve the user's information,
    and checks the validity of the token. If the token is valid, the request is allowed to proceed to the
    route function with the user's information passed as keyword arguments. If the token is invalid or expired,
    or if any other exception occurs during the process, the request is denied with a 401 Unauthorized status.

    The decoded information includes user ID, organisation ID list, and email, which are used for further
    validation or within the route function.

    Parameters:
    - route_function (function): The route function to wrap. This is the function that the decorator is applied to.

    Returns:
    - If token is valid: The result of the `route_function` with additional keyword arguments (`user_id`, `user_org_id_list`).
    - If token is invalid or missing, or if an exception occurs: A dictionary with an "error" key and a 401 HTTP status.

    Notes:
    - The decorator expects the JWT to be in the 'Authorization' header formatted as 'Bearer <token>'.
    - The `decode_jwt` function is responsible for decoding the JWT and extracting the required information.
    - The `is_jwt_valid` function is responsible for checking the expiration time of the token.
    - Uses `functools.wraps` to preserve the metadata of the original `route_function`.
    - Logs a warning message with the user's email and the accessed route name if the token validation fails.
    """

    @wraps(route_function)
    def wrapper(*args, **kwargs):
        username = "Unknown"  # Initialize username as "Unknown" before decoding
        try:
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                return jsonify(message="Session expired, please login again."), 401

            user_jwt = auth_header.replace("Bearer ", "")
            exp_time, user_id, username = decode_jwt(user_jwt)

            if not is_jwt_valid(exp_time):
                return (
                    jsonify(message="Session expired, please login again."),
                    401,
                )

            return route_function(
                user_id=user_id,
                username=username,
                *args,
                **kwargs,
            )
        except jwt.DecodeError as err:
            print(err)
            return jsonify(message="Session expired, please login again."), 401
        except jwt.ExpiredSignatureError as err:
            print(err)
            return jsonify(message="Session expired, please login again."), 401
        except Exception as err:
            print(err)
            return jsonify(message="Session expired, please login again."), 401

    return wrapper
