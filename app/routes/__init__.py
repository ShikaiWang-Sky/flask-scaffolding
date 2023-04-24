from flask import Flask

from app.routes.auth import auth_bp
from routes.home import home_bp


def init_app(app: Flask) -> None:
    """
    Register blueprints, new files added to routes folder should be registered here
    :param app: Flask app
    :return: None
    """
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
