import flask
import flask_sqlalchemy

from application import views
from application.posts import views

app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = flask_sqlalchemy.SQLAlchemy(app)

db.create_all()
