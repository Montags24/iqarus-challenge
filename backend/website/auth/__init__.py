from flask import Blueprint

# Blueprint Configuration
bp_folder = "auth"
bp = Blueprint(
    f"{bp_folder}_bp",
    __name__,
    template_folder="templates",
    static_folder="assets",
)
from website.auth import routes

routes = routes
