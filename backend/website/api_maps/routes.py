from datetime import datetime, timedelta
from flask import request, jsonify
from website import db
from website.api_maps import bp
from website.models import SecurityForm, CommunicationsForm, InfrastructureForm
from website.api_users.utilities import validate_user


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
        date_from = datetime.strptime(api_package["dateFrom"], "%Y-%m-%d")
        # We add a day here as the query doesn't pick up same day even though using <=
        date_to = datetime.strptime(api_package["dateTo"], "%Y-%m-%d") + timedelta(
            days=1
        )
        search_latitude = api_package["searchLatitude"]
        search_longitude = api_package["searchLongitude"]
        search_radius_km = api_package["searchRadiusKm"]
    except KeyError:
        return jsonify(message="Bad API request - please try again"), 400
    except Exception:
        return jsonify(message="An error occurred"), 500

    if len(categories) == 0:
        return jsonify(message="No categories selected"), 204

    if search_latitude is None or search_longitude is None:
        return (
            jsonify(message="A location must be selected to initiate the search"),
            204,
        )

    if search_radius_km is None:
        return (
            jsonify(message="A search radius must be supplied"),
            204,
        )

    category_mapping = {
        "security": SecurityForm,
        "communications": CommunicationsForm,
        "infrastructure": InfrastructureForm,
    }
    forms_to_search = [category_mapping[category] for category in categories]

    results = []

    # Really inefficient way to search for locations within radius, but for now it'll do.
    # In the future look into postGIS
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
