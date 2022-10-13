from select import select
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Directory(object):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)    

    @property
    def is_new(self):
        return self.id == None
        

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
    

class Point(db.Model, Directory):
    
    short = db.Column(db.String(10))

    def __repr__(self) -> str:
        return f"<Point {self.title}, {self.id}>"
