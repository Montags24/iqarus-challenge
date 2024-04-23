from datetime import datetime


def convert_ms_to_datetime(time_in_ms):
    # Convert milliseconds timestamp to seconds
    timestamp_seconds = time_in_ms / 1000.0

    # Create a Python datetime object from the timestamp
    datetime_obj = datetime.fromtimestamp(timestamp_seconds)

    return datetime_obj
