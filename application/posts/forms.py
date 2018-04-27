from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, validators


class PostForm(FlaskForm):
    content = TextAreaField("Content", [validators.Length(min=2)])

    class Meta:
        csrf = False
