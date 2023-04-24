import json
import os

import firebase_admin
import pyrebase
from firebase_admin import credentials, auth as firebase_auth
from flask import Blueprint, redirect, url_for, session, render_template, request

from app.utils.decorators.auth_decorator import login_required
from forms.auth_forms import LoginForm, SignupForm
from log import Log

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
basedir = os.path.abspath(os.path.dirname(__file__))
firebase_config_path = os.path.normpath(os.path.join(basedir, "../config/firebase"))

# Connect to firebase
cred = credentials.Certificate(
    os.path.join(firebase_config_path, "firebaseAdminConfig.json")
)
firebase = firebase_admin.initialize_app(cred)
# pyrebase4 which is a python wrapper for firebase
pb = pyrebase.initialize_app(
    json.load(open(os.path.join(firebase_config_path, "firebaseConfig.json")))
)


# auth routes, user click login button, redirect to login page
@auth_bp.route("/")
def auth():
    form = LoginForm()
    return render_template("login.html", form=form)


@auth_bp.route("/redirect_to_signup")
def redirect_to_signup():
    """Redirect to signup page"""
    form = SignupForm()
    return render_template("signup.html", form=form)


@auth_bp.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        email = request.form.get("email")
        password = request.form.get("password")
        try:
            user = firebase_auth.create_user(email=email, password=password)
            uid = user.uid
            Log.logger().info(f"User {uid} signed up")
            return redirect(url_for("auth.login", _scheme="http", _external=True))
        except Exception as e:
            Log.logger().error(f"Error when signing up: {e}")
            message = "Error when signing up, please try again"
            return render_template("login.html", message=message, form=form)
    return render_template("signup.html", form=form)


@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = request.form.get("email")
        password = request.form.get("password")
        try:
            user = pb.auth().sign_in_with_email_and_password(email, password)
            Log.logger().info(f"User{user} logged in")
            uid = user["localId"]
            session["user_id"] = uid
            return redirect(url_for("home.home_page", _scheme="http", _external=True))
        except Exception as e:
            Log.logger().error(f"Error when logging in: {e}")
            message = "Error when logging in, please try again"
            return render_template("login.html", message=message, form=form)
    return render_template("login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    """
    User logout
    clear session
    :return: redirect to index
    """
    user_id = session.get("user_id")
    session.clear()
    Log.logger().info(f"User {user_id} logged out")
    return redirect(url_for("home.home_page", _scheme="http", _external=True))
