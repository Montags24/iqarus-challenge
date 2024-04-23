import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()

# create the holder for site config stuff
site_config = {}
site_config["instance_type"] = os.environ.get("instance_type")
site_config["this_url"] = os.environ.get("this_url")


def create_app():
    # This constructs the Flask application instance, and eliminates using it as a global variable, which can cause issues

    # Set the paths so that Flask knows where to look to serve up the static files
    this_directory = os.path.abspath(os.path.dirname(__file__))
    static_folder = os.path.join(this_directory, "templates", "assets")
    app = Flask(
        __name__,
        instance_relative_config=False,
        static_folder=static_folder,
    )

    # enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # app.config.from_object("config.Config")
    app.config.from_object(Config)

    with app.app_context():
        # now all the initiations
        db.init_app(app)
        migrate.init_app(app, db=db)

        from website.api_users import bp as users_bp

        app.register_blueprint(users_bp, url_prefix="/api/users")

        from website.auth import bp as auth_bp

        app.register_blueprint(auth_bp, url_prefix="/api/auth")

        from website.api_forms import bp as forms_bp

        app.register_blueprint(forms_bp, url_prefix="/api/forms")

        from website.frontend import bp as frontend_bp

        app.register_blueprint(frontend_bp, url_prefix="/")

        # from website import routes, models

        # # To satisfy pylint
        # routes, models = routes, models

        return app
