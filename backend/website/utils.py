from math import radians, sin, cos, sqrt, atan2


def calculate_haversine(center_lat, center_long, target_lat, target_long):
    """
    Returns the great-circle distance in kilometers between the instance and a point.
    """
    R = 6371  # Earth's radius in kilometers

    dlat = radians(center_lat - target_lat)
    dlng = radians(center_long - target_long)

    a = (
        (sin(dlat / 2) * sin(dlat / 2) + cos(radians(target_lat))).real
        * cos(radians(center_lat).real)
        * sin(dlng / 2)
        * sin(dlng / 2)
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a)).real

    d = R * c

    return d


def calculate_longitude_degrees_for_km(distance_km, latitude_deg):
    """
    Returns the longitude in degrees for a given distance at a given latitude
    """
    # Constants
    km_per_degree_latitude = 111

    # Calculate the distance for one degree of longitude at the given latitude
    latitude_rad = radians(latitude_deg)
    km_per_degree_longitude = km_per_degree_latitude * cos(latitude_rad)

    # Convert the distance from kilometers to degrees of longitude
    degrees_longitude = distance_km / km_per_degree_longitude
    return degrees_longitude


def calculate_km_to_latitude_degrees(km):
    """
    Convert a distance in kilometers to degrees of latitude.

    Parameters:
    km (float): Distance in kilometers.

    Returns:
    float: Distance in degrees of latitude.
    """
    # One degree of latitude is approximately 111 kilometers
    km_per_degree = 111.0
    degrees = km / km_per_degree
    return degrees
