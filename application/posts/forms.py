from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, validators


class PostForm(FlaskForm):
    content = TextAreaField("Content", [validators.Length(message="limit 2-2000 characters", min=2, max=2000)])

    class Meta:
        csrf = False
