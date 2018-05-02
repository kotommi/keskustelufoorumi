from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class CategoryForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=3, message="Title should be at least 3 characters")])
    description = TextAreaField("Description", [validators.Length(min=3, message="Not nullable, min length 3")])
