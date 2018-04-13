from application import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Integer, default=db.func.current_timestamp())
    date_modified = db.Column(db.Integer, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

