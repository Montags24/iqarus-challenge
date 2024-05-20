from datetime import datetime, timedelta
from flask import request, jsonify
from website import db
from website.api_maps import bp
from website.models import SecurityForm, CommunicationsForm, InfrastructureForm
from website.utils import (
    calculate_longitude_degrees_for_km,
    calculate_km_to_latitude_degrees,
)


@bp.route("/", methods=["POST"])
def get_form_data_for_maps():
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

    # First specify a 50x50km box to search from (this is the max radius we set)
    # Filter the results from that search
    # For latitude, 1 degree is approx 111km
    # 50km is approx 0.45 degrees of latitude
    # For longitude,
    for form in forms_to_search:

        latitude_degree_range = calculate_km_to_latitude_degrees(search_radius_km * 2)
        longitude_degree_range = calculate_longitude_degrees_for_km(
            search_radius_km * 2, search_latitude
        )
        lower_bound_latitude = search_latitude - (latitude_degree_range / 2)
        upper_bound_latitude = search_latitude + (latitude_degree_range / 2)

        lower_bound_longitude = search_longitude - (longitude_degree_range / 2)
        upper_bound_longitude = search_longitude + (longitude_degree_range / 2)

        form_entries = (
            db.session.query(form)
            .filter(form.timestamp <= date_to, date_from <= form.timestamp)
            .filter(
                form.latitude <= upper_bound_latitude,
                lower_bound_latitude <= form.latitude,
            )
            .filter(
                form.longitude <= upper_bound_longitude,
                lower_bound_longitude <= form.longitude,
            )
            .all()
        )

        for entry in form_entries:
            if entry.distance_to(search_latitude, search_longitude) < search_radius_km:
                results.append(entry.get_dict())

    return jsonify(results=results)
