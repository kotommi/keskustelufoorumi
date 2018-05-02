from flask_wtf import FlaskForm
from wtforms import StringField, validators


class AdminForm(FlaskForm):
    username = StringField("Username to promote to admin", validators=[validators.Length(min=4)])

    class Meta:
        csrf = False
