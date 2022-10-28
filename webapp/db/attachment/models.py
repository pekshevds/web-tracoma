from webapp.db.common import db, Directory
from webapp.db import Order


class Attachment(db.Model, Directory):
    weight = db.Column(db.Float)
    volume = db.Column(db.Float)
    height = db.Column(db.Float)
    width = db.Column(db.Float)
    depth = db.Column(db.Float)
    order_id = db.Column(db.Integer, db.ForeignKey(Order.id), nullable=True)

    def __repr__(self) -> str:
        return f"<Attachment {self.title}, {self.id}>"
