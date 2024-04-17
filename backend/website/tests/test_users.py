import pytest
import secrets
import os
from dotenv import load_dotenv
from sqlalchemy import true
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


def test_create_user(client):
    route = "api/users/"
    # token = secrets.token_urlsafe(5)
    # password = secrets.token_urlsafe(10)
    new_user_credentials = dict(
        name="test_api_user",
        email="test_api_user_@example.com",
        password="fake_password",
    )
    payload_kwargs = dict(new_user_credentials=new_user_credentials)
    response = client.post(route, json=payload_kwargs)

    assert response.status_code == 200
    assert response.json["message"] == "The user was successfully created."
