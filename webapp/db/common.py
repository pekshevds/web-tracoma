from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Directory(object):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    is_deleted = db.Column(db.Boolean, default=False)
    create_date = db.Column(db.DateTime, default=datetime.now())
    update_date = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)

    @property
    def is_new(self):
        return self.id == (None)
