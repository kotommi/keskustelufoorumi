import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    print("using psql at: " + os.environ.get("DATABASE_URL"))
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from application.category import models
from application.category import views

from application.auth import models
from application.auth import views

from application import views
from application.posts import views
from application.posts import models

from application.threads.models import Thread
from application.threads import views
from application.threads import models

# login
from application.auth.models import User
from os import urandom

app.config["SECRET_KEY"] = urandom(32)

db.create_all()

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
