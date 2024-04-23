import os
from dotenv import load_dotenv


this_directory = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(this_directory, "...", ".env"), override=True)


def get_session_and_mfa_jwt(client, user_type):
    try:
        login_endpoint = "/api/auth/login"
        login_credentials = dict(
            username=os.environ.get(f"{user_type}_username"),
            password=os.environ.get(f"{user_type}_password"),
        )

        response = client.post(login_endpoint, json=login_credentials)
        response_package = response.json
        session_jwt = response_package["package"]["session_jwt"]

        return session_jwt
    except Exception as err:
        print(f"Response failed - {err}")


def get_headers(client):
    session_jwt = get_session_and_mfa_jwt(client, "super_user")
    user_headers = {"Authorization": f"Bearer {session_jwt}"}

    invalid_headers = {"Authorization": "Bearer invalid"}

    return dict(
        user=user_headers,
        invalid=invalid_headers,
    )
