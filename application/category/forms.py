from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class CategoryForm(FlaskForm):
    title = StringField("Title",
                        validators=[validators.Length(min=3, max=144, message="Title should be 3-144 characters")])
    description = TextAreaField("Description",
                                validators=[validators.Length(min=3, max=255, message="Not nullable, length 3-255")])

    class Meta:
        csrf = False
