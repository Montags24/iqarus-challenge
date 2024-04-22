import pytest
import secrets
import os
from dotenv import load_dotenv
from website import create_app, db
from website.models import (
    User,
)


THIS_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(THIS_DIRECTORY, "...", ".env"), override=True)


app = create_app()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            yield client


# Fixture for authentication
# @pytest.fixture
# def headers(client):
#     headers = get_headers(client)
#     return headers


def test_successful_login(client):
    # Create a user
    route = "api/users/"
    token = secrets.token_urlsafe(5)
    password = secrets.token_urlsafe(10)
    new_user_credentials = dict(
        name=f"test_api_user_{token}",
        username=f"test_api_username_{token}",
        password=f"{password}",
    )

    response = client.post(route, json=new_user_credentials)

    assert response.status_code == 201
    assert response.json["message"] == "The user was successfully created."

    user = User.query.filter_by(username=new_user_credentials["username"]).first()
    assert user

    # Attempt login
    route = "api/auth/login"
    login_package = {
        "username": new_user_credentials["username"],
        "password": password,
    }

    response = client.post(route, json=login_package)
    assert response.status_code == 200

    # Delete user
    User.query.filter_by(username=new_user_credentials["username"]).delete()
    db.session.commit()
    user = User.query.filter_by(username=new_user_credentials["username"]).first()
    assert user is None


def test_login_incorrect_password(client):
    # Create a user
    route = "api/users/"
    token = secrets.token_urlsafe(5)
    password = secrets.token_urlsafe(10)
    new_user_credentials = dict(
        name=f"test_api_user_{token}",
        username=f"test_api_username_{token}",
        password=f"{password}",
    )

    response = client.post(route, json=new_user_credentials)

    assert response.status_code == 201
    assert response.json["message"] == "The user was successfully created."

    user = User.query.filter_by(username=new_user_credentials["username"]).first()
    assert user

    # Attempt login with incorrect password
    route = "api/auth/login"
    login_package = {
        "username": new_user_credentials["username"],
        "password": "fake_password",
    }

    response = client.post(route, json=login_package)
    assert response.status_code == 401

    # Delete user
    User.query.filter_by(username=new_user_credentials["username"]).delete()
    db.session.commit()
    user = User.query.filter_by(username=new_user_credentials["username"]).first()
    assert user is None
