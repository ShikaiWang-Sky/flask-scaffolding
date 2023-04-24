# Desc: Forms for authentication
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    """Login Form validation"""

    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    submit = SubmitField("LOGIN")


class SignupForm(FlaskForm):
    """Signup Form validation"""

    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    password_confirm = PasswordField(
        "Confirm Password",
        validators=[InputRequired(), Length(min=6), EqualTo("password")],
    )
    submit = SubmitField("SIGNUP")
