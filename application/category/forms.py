from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, validators
from application.auth.models import Role


class CategoryForm(FlaskForm):
    title = StringField("Title")
    description = TextAreaField("Description")
    roles = SelectField("Allowed roles")
