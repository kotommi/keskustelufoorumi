from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, validators


class PostForm(FlaskForm):
    content = TextAreaField("Content", [validators.Length(message="limit 2-1000 characters",min=2, max=1000)])

    class Meta:
        csrf = False
