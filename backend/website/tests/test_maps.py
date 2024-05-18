import pytest
import os
import secrets
from datetime import datetime, timedelta, timezone
import random
from dotenv import load_dotenv
from website import create_app, db
from website.models import SecurityForm, User
from website.tests.utilities import get_headers


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
@pytest.fixture
def headers(client):
    headers = get_headers(client)
    return headers


def convert_date_to_ms(date):
    return int(date.timestamp() * 1000)


def test_get_form_data_for_maps(client, headers):
    # Add a response to the security form
    route = "api/forms/security"
    token = secrets.token_urlsafe(5)

    latitude = random.randint(-90, 90)
    longitude = random.randint(-180, 180)

    payload = {
        "timestamp": convert_date_to_ms(datetime.now(tz=timezone.utc)),
        "latitude": latitude,
        "longitude": longitude,
        "armedGroupsPresence": f"{token}_armedGroupsPresence",
        "reportOfViolence": f"{token}_reportOfViolence",
        "localEnforcementPresence": f"{token}_localEnforcementPresence",
        "securityRiskComments": f"{token}_securityRiskComments",
        "incidentsReported": f"{token}_incidentsReported",
        "riskToRelief": f"{token}_riskToRelief",
        "incidentsComments": f"{token}_incidentsComments",
    }

    response = client.post(route, headers=headers["user"], json=payload)

    # Get id to delete later
    id = response.json["form"]["id"]
    assert response.status_code == 201

    route = "api/maps/"

    now = datetime.now().date()
    one_week_ago = now - timedelta(weeks=1)

    payload = {
        "categories": ["security"],
        "dateFrom": one_week_ago.strftime("%Y-%m-%d"),
        "dateTo": now.strftime("%Y-%m-%d"),
        "searchLatitude": latitude,
        "searchLongitude": longitude,
        "searchRadiusKm": 5,
    }

    response = client.post(route, headers=headers["user"], json=payload)

    assert response.status_code == 200
    assert len(response.json["results"]) >= 1

    # Delete form entry
    db.session.query(SecurityForm).filter(id == id).delete()
    db.session.commit()

    # Ensure entry was deleted
    entry = db.session.query(SecurityForm).filter(id == id).first()
    assert entry is None
