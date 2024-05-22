import pytest
import os
import secrets
from datetime import datetime, timezone
from dotenv import load_dotenv
from website import create_app, db
from website.models import SecurityForm
from website.tests.utilities import get_headers, convert_date_to_ms


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


def test_add_form(client, headers):
    route = "api/forms/security"
    token = secrets.token_urlsafe(5)

    payload = {
        "timestamp": convert_date_to_ms(datetime.now(tz=timezone.utc)),
        "latitude": 40.0,
        "longitude": 40.0,
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

    # Delete form entry
    db.session.query(SecurityForm).filter(id == id).delete()
    db.session.commit()

    # Ensure entry was deleted
    entry = db.session.query(SecurityForm).filter(id == id).first()
    assert entry is None
