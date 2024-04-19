from flask import Blueprint

# Blueprint Configuration
bp_folder = "users"
bp = Blueprint(
    f"{bp_folder}_bp",
    __name__,
    template_folder="templates",
    static_folder="assets",
)

from website.api_users import routes

routes = routes
