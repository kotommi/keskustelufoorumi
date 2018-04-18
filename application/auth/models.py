from application import db
from application.models import Base
from sqlalchemy.sql import text


class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    posts = db.relationship("Post", backref="account", lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]

    @staticmethod
    def find_usernames():
        statement = text(
            "SELECT account.name, account.username FROM account")
        res = db.engine.execute(statement)

        response = []
        for row in res:
            response.append({row[0]})
            response.append({row[1]})

        return response

    @staticmethod
    def find_users_with_no_posts():
        statement = text(
            "SELECT account.id, account.name FROM account LEFT JOIN Post ON Post.account_id = account.id GROUP  BY account.id HAVING COUNT(Post.id) = 0")
        res = db.engine.execute(statement)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1]})
        return response
