from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from application.auth.models import User


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class CreateForm(FlaskForm):
    username = StringField("Username",
                           [validators.Length(min=4, max=16, message="Name has to be at least 4 characters"),
                            validators.any_of(User.find_usernames(),
                                              message="Name already in use")])
    password = PasswordField("Password",
                             [validators.Length(min=8, max=32, message="Password has to be at least 8 characters")])
    repeat_password = PasswordField(
        "Repeat password", [validators.EqualTo(password, message="Passwords must match")])


class Meta:
    csrf = False
