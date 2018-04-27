from application import db
from application.models import Base

category_role = db.Table('category_role', Base.metadata,
                         db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
                         db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
                         )


class Category(Base):
    __tablename__ = "category"

    title = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    threads = db.relationship("Thread", backref="category", lazy=True)
    roles = db.relationship("Role", secondary=category_role, backref="Category")

    def __init__(self, title, description, roles=None):
        """
        :type title: String
        :type description: String
        """
        if roles is None:
            roles = ["normal"]
        self.title = title
        self.description = description
        self.roles = roles.copy()
