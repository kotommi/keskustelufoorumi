from application import db
from application.models import Base
from sqlalchemy import text


class Thread(Base):
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(2000), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)

    posts = db.relationship("Post", backref="Thread", lazy=True, cascade="all, delete-orphan")

    def __init__(self, title, content, category_id, user_id):

        self.title = title
        self.content = content
        self.category_id = category_id
        self.user_id = user_id

    @staticmethod
    def find_recent(i=5):
        statement = text(
            "SELECT * FROM thread ORDER BY date_modified DESC LIMIT :many").params(many=i)
        res = db.engine.execute(statement)

        response = []
        for row in res:
            thread = Thread(title=row[3], content=row[4], category_id=row[5], user_id=row[6])
            thread.id = row[0]
            response.append(thread)
        return response

    @staticmethod
    def find_latest_threads(user_id, i=5):
        statement = text(
            "SELECT * FROM thread WHERE thread.user_id = :user_id ORDER BY date_modified DESC LIMIT :i"
        ).params(user_id=user_id, i=i)
        res = db.engine.execute(statement)
        response = []
        for row in res:
            thread = Thread(title=row[3], content=row[4], category_id=row[5], user_id=row[6])
            thread.id = row[0]
            response.append(thread)
        return response
