from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class PostForm(FlaskForm):
    name = StringField("Title", [validators.Length(min=2)])
    content = TextAreaField("Content", [validators.Length(min=2)])

    class Meta:
        csrf = False
