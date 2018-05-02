from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class CategoryForm(FlaskForm):
    title = StringField("Title",
                        validators=[validators.Length(min=3, max=100, message="Title should be at least 3 characters")])
    description = TextAreaField("Description",
                                validators=[validators.Length(min=3, max=999, message="Not nullable, min length 3")])

    class Meta:
        csrf = False
