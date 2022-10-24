from webapp.db.common import db, Directory
from webapp.db.storage.fetchers import get_storage_by_id
from webapp.db.point.fetchers import get_point_by_id
from datetime import datetime


class Order(db.Model, Directory):
    carrier_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    consignee_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    consignee_address = db.Column(db.String(255))
    consignee_contact_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=True)
    consignee_phone = db.Column(db.String(255))
    declared = db.Column(db.Float)
    desc = db.Column(db.Text)
    point_from_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    point_to_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    shipper_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    shipper_address = db.Column(db.String(255))
    shipper_contact_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=True)
    shipper_phone = db.Column(db.String(255))
    weight = db.Column(db.Float)
    volume = db.Column(db.Float)

    def __repr__(self) -> str:
        return f"<Cargo {self.title}, {self.id}>"

    def __str__(self) -> str:
        return f"Order #{self.id} of {datetime.strftime(self.create_date, '%Y-%m-%d')}"

    @property
    def carrier(self):
        return get_storage_by_id(self.carrier_id)

    @property
    def consignee(self):
        return get_storage_by_id(self.consignee_id)

    @property
    def shipper(self):
        return get_storage_by_id(self.shipper_id)

    @property
    def point_from(self):
        return get_point_by_id(self.point_from_id)

    @property
    def point_to(self):
        return get_point_by_id(self.point_to_id)
