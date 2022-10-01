from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    is_mark = db.Column(db.Boolean)

    is_internal = db.Column(db.Boolean)
    is_employee = db.Column(db.Boolean)
    kind = db.Column(db.Integer, nullable=False)
    inn = db.Column(db.String(13))
    kpp = db.Column(db.String(10))
    weight = db.Column(db.Float)
    volume = db.Column(db.Float)

    def __repr__(self) -> str:
        return self.title

    def __str__(self) -> str:
        return self.title


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    is_mark = db.Column(db.Boolean)

    short = db.Column(db.String(10))
    
    def __repr__(self) -> str:
        return self.title

    def __str__(self) -> str:
        return self.title
