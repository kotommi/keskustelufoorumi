from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, HiddenField
from application.auth.models import User
from application.category.models import Category


class ThreadForm(FlaskForm):
    title = StringField("Title", [validators.Length(message="Min 4, max 255 characters", min=4, max=255)])
    content = TextAreaField("Content", [validators.Length(message="Min 5, max 2000 characters", min=5, max=2000)])
    user_id = HiddenField(User.id)
    cat_id = HiddenField(Category.id)

    class Meta:
        csrf = False
