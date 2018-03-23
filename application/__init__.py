import flask
import flask_sqlalchemy


app = flask.Flask(__name__)
db = flask_sqlalchemy.SQLAlchemy(app)


from application import views
from application.posts import views

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.create_all()
