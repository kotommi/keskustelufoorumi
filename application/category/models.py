from application import db


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    title = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    posts = db.relationship("Post", backref="category", lazy=True)

    def __init__(self, title, description):
        """
        :type title: String
        :type description: String
        """
        self.title = title
        self.description = description
