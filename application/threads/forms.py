from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, HiddenField
from application.auth.models import User
from application.category.models import Category


class ThreadForm(FlaskForm):
    title = StringField("Title", [validators.Length(message="Min 4, max 144 characters", min=4, max=144)])
    content = TextAreaField("Content", [validators.Length(message="Min 5, max 1000 characters", min=5, max=1000)])
    user_id = HiddenField(User.id)  # missä validointi?
    cat_id = HiddenField(Category.id)  # sama kuin ^

    class Meta:
        csrf = False
