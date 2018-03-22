import application


class Post(application.db.Model):
    id = application.db.Column(application.db.Integer, primary_key=True)
    date_created = application.db.Column(application.db.DateTime, default=application.db.func.current_timestamp())
    date_modified = application.db.Column(application.db.DateTime, default=application.db.func.current_timestamp(),
                                          onupdate=application.db.func.current_timestamp())

    name = application.db.Column(application.db.String(144), nullable=False)
    content = application.db.Column(application.db.String(1000), nullable=False)

    def __init__(self, name, content):
        self.name = name
        self.content = content
