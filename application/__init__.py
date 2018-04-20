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
from application.auth import models
from application.role import models
from application.posts import models
from application.threads.models import Thread
from application.threads import models
from application.auth.models import User

# create tables if not present
db.create_all()

# login
from os import urandom

app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# decorator for roles in login_required
from functools import wraps


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)

        return decorated_view

    return wrapper


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# load views
from application.auth import views
from application.category import views
from application.threads import views
from application import views
from application.posts import views
