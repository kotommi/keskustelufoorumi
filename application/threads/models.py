import application


class Thread(application.db.Model):
    id = application.db.Column(application.db.Integer, primary_key=True)
    date_created = application.db.Column(application.db.DateTime, default=application.db.func.current_timestamp())
    date_modified = application.db.Column(application.db.DateTime, default=application.db.func.current_timestamp(),
                                          onupdate=application.db.func.current_timestamp())

    title = application.db.Column(application.db.String(144), nullable=False)
    content = application.db.Column(application.db.String(1000), nullable=False)

    def __init__(self, title, content):
        """
        :type title: String
        :type content: String
        """
        self.title = title
        self.content = content
