from application import db
from application.models import Base


class Thread(Base):
    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(1000), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)

    posts = db.relationship("Post", backref="Thread", lazy=True)

    def __init__(self, title, content):
        """
        :type title: String
        :type content: String
        """
        self.title = title
        self.content = content
