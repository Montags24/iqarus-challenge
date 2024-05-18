from flask import Blueprint

# Blueprint Configuration
bp_folder = "forms"
bp = Blueprint(
    f"{bp_folder}_bp",
    __name__,
    template_folder="templates",
    static_folder="assets",
)

from website.api_forms import routes

routes = routes
