from flask import request, jsonify
from website import db
from website.api_forms import bp
from website.models import SecurityForm, CommunicationsForm, InfrastructureForm
from website.api_users.utilities import validate_user
from website.api_forms.utilities import convert_ms_to_datetime


# Add form entry to database
@bp.route("/<category>", methods=["POST"])
@validate_user
def add_form(category: str, **kwargs):
    try:
        api_package = request.get_json()
    except KeyError:
        return jsonify(message="Bad api request - please try again"), 400
    except Exception:
        return jsonify(message="An error occured"), 500

    try:
        api_package["user_id"] = kwargs["user_id"]
        api_package["timestamp"] = convert_ms_to_datetime(api_package["timestamp"])

        # update form model with api package data
        form_to_update = get_form_model(category)
        for name, value in api_package.items():
            if hasattr(form_to_update, name):
                setattr(form_to_update, name, value)
        db.session.add(form_to_update)
        db.session.commit()
        form_dict = form_to_update.get_dict()

        return (
            jsonify(message="The form was successfully submitted.", form=form_dict),
            201,
        )
    except Exception as err:
        print(err)
        db.session.rollback()
        db.session.flush()  # for resetting non-commited .add()
        return jsonify(message="An error occured submitting a form"), 500


def get_form_model(category: str) -> object:
    if category == "security":
        return SecurityForm()
    elif category == "infrastructure":
        return InfrastructureForm()
    elif category == "communications":
        return CommunicationsForm()


# Add form entry to database
@bp.route("/", methods=["POST"])
@validate_user
def add_offline_forms(**kwargs):
    try:
        api_package = request.get_json()
    except KeyError:
        return jsonify(message="Bad api request - please try again"), 400
    except Exception:
        return jsonify(message="An error occured"), 500

    try:
        submitted_forms = []
        for entry in api_package["payload"]:
            entry["timestamp"] = convert_ms_to_datetime(entry["timestamp"])
            entry["user_id"] = kwargs["user_id"]

            # update form model with api package data
            form_to_update = get_form_model(entry["formName"])
            for name, value in entry.items():
                if hasattr(form_to_update, name):
                    setattr(form_to_update, name, value)
            db.session.add(form_to_update)
            db.session.commit()
            submitted_forms.append(form_to_update.get_dict())

        return (
            jsonify(
                message="The forms were successfully submitted.", forms=submitted_forms
            ),
            201,
        )
    except Exception as err:
        print(err)
        db.session.rollback()
        db.session.flush()  # for resetting non-commited .add()
        return jsonify(message="An error occured submitting a form"), 500
