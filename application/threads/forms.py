from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, HiddenField
from application.auth.models import User
from application.category.models import Category


class ThreadForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=4)])
    content = TextAreaField("Content", [validators.Length(min=10)])
    user_id = HiddenField(User.id)  # missä validointi?
    cat_id = HiddenField(Category.id)  # sama kuin ^

    class Meta:
        csrf = False
