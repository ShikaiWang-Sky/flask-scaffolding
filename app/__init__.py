from flask import Flask
from flask_wtf import CSRFProtect

from app import routes
from app.extensions import db, csrf
from config.config import config

from log import Log


def create_app(config_name="default"):
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # register blueprints
    routes.init_app(app)

    # initialize extensions here
    # initialize sqlalchemy
    db.init_app(app)
    # initialize csrf
    csrf.init_app(app)

    # initialize log
    Log.init_app(app)

    # log info when app is created
    Log.logger().info(f"Creating app with config: {config_name}")

    # test route
    @app.route("/test")
    def test():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app
