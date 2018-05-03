import flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.utils import hash_password

# App configs
app = flask.Flask(__name__)

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    print("using psql at: " + os.environ.get("DATABASE_URL"))
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config[
    "SECURITY_PASSWORD_SALT"] = "super secret salt"  # this is just for the hmac, not actual passwords
app.config["SECURITY_PASSWORD_HASH"] = "bcrypt"

from os import urandom

app.config["SECRET_KEY"] = urandom(32)

db = SQLAlchemy(app)

# Models
from application.category import models
from application.auth import models
from application.posts import models
from application.threads.models import Thread
from application.threads import models
from application.auth.models import User, Role

# Create tables if not present
db.create_all()

# Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# login

from flask_security.core import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    if (User.query.filter_by(username="testadmin")).first() is None:
        admin = user_datastore.create_user(name="testadmin", username="testadmin", password=hash_password("asdasdasd"))
        db.session.commit()
        user_datastore.add_role_to_user(admin, user_datastore.find_or_create_role("admin"))
        user_datastore.activate_user(admin)
        user_datastore.commit()


# load views
from application.auth import views
from application.category import views
from application.threads import views
from application import views
from application.posts import views
from application.control import views
