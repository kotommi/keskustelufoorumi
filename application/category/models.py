from application import db
from application.models import Base


class Category(Base):
    __tablename__ = "category"

    title = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    threads = db.relationship("Thread", backref="category", lazy=True)


    def __init__(self, title, description):
        """
        :type title: String
        :type description: String
        """
        self.title = title
        self.description = description
