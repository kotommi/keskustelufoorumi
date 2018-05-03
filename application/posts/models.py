from application import db
from application.models import Base
from application.auth.models import User
from sqlalchemy import text


class Post(Base):
    name = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(2000), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey("thread.id"), nullable=False)

    def __init__(self, content, name="reply"):
        self.name = name
        self.content = content

    @staticmethod
    def find_recent(i=5):
        statement = text(
            "SELECT * FROM post ORDER BY date_modified DESC LIMIT :many").params(many=i)
        res = db.engine.execute(statement)

        response = []
        for row in res:
            post = Post((row[4]))
            post.thread_id = row[6]
            response.append(post)
        return response

    @staticmethod
    def find_latest_posts(user_id, i=5):
        statement = text(
            "SELECT * FROM post WHERE post.account_id = :user_id ORDER BY date_modified DESC LIMIT :many"
        ).params(user_id=user_id, many=i)
        res = db.engine.execute(statement)
        response = []
        for row in res:
            post = Post((row[4]))
            post.thread_id = row[6]
            response.append(post)
        return response
