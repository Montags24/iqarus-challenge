from flask import request, jsonify
from website import db
from website.api_forms import bp
from website.models import SecurityForm, CommunicationsForm, InfrastructureForm
from website.api_users.utilities import validate_user
from website.api_forms.utilities import convert_ms_to_datetime


# User CRUD
@bp.route("/")
@validate_user
def add_form(**kwargs):
    return
