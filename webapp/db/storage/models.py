from webapp.db.common import db, Directory
from sqlalchemy.orm import relationship


class Storage(db.Model, Directory):
    is_internal = db.Column(db.Boolean, default=False)
    is_employee = db.Column(db.Boolean, default=False)
    kind = db.Column(db.Integer, nullable=False)
    inn = db.Column(db.String(13))
    kpp = db.Column(db.String(10))
    weight = db.Column(db.Float)
    volume = db.Column(db.Float)

    def __repr__(self) -> str:
        return f"<Storage {self.title}, {self.id}>"

    def __str__(self) -> str:
        return self.title
