from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class CreateForm(FlaskForm):
    username = StringField("Username", validators.Length(min=4))  # lisää check onko käytössä
    password = PasswordField("Password", validators.Length(min=8))
    repeat_password = PasswordField("Repeat password", validators.EqualTo('password'), message="Passwords must match")

    class Meta:
        csrf = False
