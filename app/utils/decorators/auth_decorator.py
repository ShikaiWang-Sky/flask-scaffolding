import functools

from flask import session, redirect, url_for

from log import Log


def login_required(view):
    """
    Decorator to ensure user is logged in before accessing a view
    :param view: view to be decorated
    :return: decorated view
    """

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        user_id = session.get("user_id")
        if user_id is None:
            Log.logger().info("User is not logged in, redirect to login page")
            return redirect(url_for("auth.login"))
        return view(**kwargs)

    return wrapped_view
