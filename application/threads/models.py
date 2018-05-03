from application import db
from application.models import Base
from sqlalchemy import text


class Thread(Base):
    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(1000), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)

    posts = db.relationship("Post", backref="Thread", lazy=True, cascade="all, delete-orphan")

    def __init__(self, title, content, category_id, user_id):
        """
        :type title: String
        :type content: String
        """
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
