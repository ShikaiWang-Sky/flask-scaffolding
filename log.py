import os
import logging
from logging import handlers
from werkzeug.exceptions import InternalServerError

basedir = os.path.abspath(os.path.dirname(__file__))


def handle_error(error):
    Log.logger().error(error)
    return error


class Log:
    # set log path and log level
    LOG_PATH = os.path.join(basedir, "logs")
    LOG_NAME = os.path.join(LOG_PATH, "log.txt")
    LOG_LEVEL = "INFO"

    current_app = None

    @staticmethod
    def init_app(app):
        Log.current_app = app
        if not os.path.exists(Log.LOG_PATH):
            os.makedirs(Log.LOG_PATH)

        # rename logs by date
        file_handler = logging.handlers.TimedRotatingFileHandler(
            Log.LOG_NAME, when="D", interval=1, backupCount=0, encoding="utf-8"
        )
        file_handler.suffix = "%Y-%m-%d.log"
        # set handler log level: lower than this level will not be handled by this handler
        # a logger can have multiple handlers
        file_handler.setLevel(Log.LOG_LEVEL)

        fmt = "%(asctime)s-%(levelname)s-%(filename)s-%(funcName)s-%(lineno)s: %(message)s"
        formatter = logging.Formatter(fmt)
        file_handler.setFormatter(formatter)

        # set logger log level: greater than or equal to this level will be handled by this logger
        app.logger.setLevel("DEBUG")
        app.logger.addHandler(file_handler)

        # under DEBUG mode, InternalServerError will not be handled by handle_error
        app.register_error_handler(InternalServerError, handle_error)

    @staticmethod
    def logger():
        return Log.current_app.logger
