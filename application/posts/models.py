from application import db
from application.models import Base


class Post(Base):
    name = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(1000), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey("thread.id"), nullable=False)

    def __init__(self, content, name="reply"):
        self.name = name
        self.content = content
