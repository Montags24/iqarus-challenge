from flask import request, jsonify
from sqlalchemy import inspect
from sqlalchemy.sql import func
from website import db
from website.api_maps import bp
from website.models import SecurityForm, CommunicationsForm, InfrastructureForm
from website.api_users.utilities import validate_user
from website.api_forms.utilities import convert_ms_to_datetime


# def haversine(lat1, lon1, lat2, lon2):
#     """
#     Calculate the great circle distance in kilometers between two points
#     on the earth (specified in decimal degrees).
#     """
#     lat1, lon1, lat2, lon2 = map(func.radians, [lat1, lon1, lat2, lon2])
#     dlat = lat2 - lat1
#     dlon = lon2 - lon1
#     a = (
#         func.sin(dlat / 2) ** 2
#         + func.cos(lat1) * func.cos(lat2) * func.sin(dlon / 2) ** 2
#     )
#     c = 2 * func.atan2(func.sqrt(a), func.sqrt(1 - a))
#     return 6371 * c  # Radius of Earth in kilometers


@bp.route("/", methods=["POST"])
@validate_user
def get_form_data_for_maps(**kwargs):
    try:
        api_package = request.get_json()
    except Exception:
        return jsonify(message="An error occurred"), 500

    try:
        categories = api_package["categories"]
        date_from = convert_ms_to_datetime(api_package["date_from"])
        date_to = convert_ms_to_datetime(api_package["date_to"])
        search_latitude = api_package["search_latitude"]
        search_longitude = api_package["search_longitude"]
        search_radius_km = api_package["search_radius_km"]
    except KeyError:
        return jsonify(message="Bad API request - please try again"), 400
    except Exception:
        return jsonify(message="An error occurred"), 500

    category_mapping = {
        "security": SecurityForm,
        "communications": CommunicationsForm,
        "infrastructure": InfrastructureForm,
    }
    forms_to_search = [category_mapping[category] for category in categories]

    results = []

    for form in forms_to_search:
        form_entries_in_date = (
            db.session.query(form)
            .filter(form.timestamp <= date_to, date_from <= form.timestamp)
            .all()
        )

        for entry in form_entries_in_date:
            if entry.distance_to(search_latitude, search_longitude) < search_radius_km:
                results.append(entry.get_dict())

    return jsonify(results=results)
