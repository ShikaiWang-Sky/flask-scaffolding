import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

dotenv_path = os.path.normpath(os.path.join(basedir, "../.env"))
load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(16)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    PRODUCTION_CONFIG = False

    # add some additional config during initialization
    @classmethod
    def init_app(cls, app):
        pass


# development config
class DevelopmentConfig(Config):
    # set debug mode
    DEBUG = True
    # not specified DATABASE_URL then use sqlite
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URL"
    ) or "sqlite:///" + os.path.normpath(os.path.join(basedir, "../../app.db"))
    # show original SQL when query
    SQLALCHEMY_ECHO = True
    PRODUCTION_CONFIG = False


# production config
class ProductionConfig(Config):
    # not specified DATABASE_URL then use sqlite
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.normpath(os.path.join(basedir, "../../app.db"))
    PRODUCTION_CONFIG = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
