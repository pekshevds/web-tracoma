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


class Order(db.Model, Directory):
    
    carrier_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    
    consignee_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    consignee_address = db.Column(db.String(255))
    consignee_contact_id = db.Column(db.Integer, db.ForeignKey('storage.id'))
    consignee_phone = db.Column(db.String(255))
    
    declared = db.Column(db.Float)
    desc = db.Column(db.Text)
    
    point_from_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    point_to_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)

    shipper_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    shipper_address = db.Column(db.String(255))
    shipper_contact_id = db.Column(db.Integer, db.ForeignKey('storage.id'))
    shipper_phone = db.Column(db.String(255))

    weight = db.Column(db.Float)
    volume = db.Column(db.Float)

    def __repr__(self) -> str:
        return f"<Cargo {self.title}, {self.id}>"
