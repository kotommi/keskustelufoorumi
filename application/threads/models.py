from application import db
from application.models import Base


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
