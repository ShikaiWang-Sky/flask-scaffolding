from flask import Blueprint, render_template, session

from log import Log

home_bp = Blueprint("home", __name__)


# home page route
@home_bp.route("/")
def home_page():
    """View function for Home Page."""
    uid = session.get("user_id")
    if uid == "" or uid is None:
        Log.logger().info("Home page accessed without login")
    else:
        Log.logger().info(f"Home page accessed by user {uid}")
    return render_template("index.html")
