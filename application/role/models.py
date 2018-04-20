from application import db
from application.models import Base

user_role = db.Table('user_role', Base.metadata,
                      db.Column('role_id', db.Integer, db.ForeignKey('Role.id')),
                      db.Column('user_id', db.Integer, db.ForeignKey('User.id'))
                      )


class Role(Base):
    __tablename__ = "Role"

    name = db.Column(db.String(50), nullable=False)
    users = db.relationship("User", secondary=user_role, backref="Role")
