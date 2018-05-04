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
                           [validators.Regexp('^\w+$',
                                              message="Username must contain only letters numbers or underscore"),
                            validators.Length(min=4, max=16, message="Name has to be at least 4 characters"),
                            validators.none_of(values=User.find_usernames(),
                                               message="Name already in use")])
    password = PasswordField("Password",
                             [validators.Length(min=8, max=32, message="Password has to be at least 8 characters"),
                              validators.EqualTo('repeat_password', message="Passwords must match")])
    repeat_password = PasswordField(
        "Repeat password")

    class Meta:
        csrf = False
