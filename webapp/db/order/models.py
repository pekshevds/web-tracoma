from webapp.db.common import db, Directory, Attachment
from webapp.db.storage.fetchers import get_storage_by_id
from webapp.db.point.fetchers import get_point_by_id
from datetime import datetime


class Order(db.Model, Directory):
    carrier_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    consignee_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    consignee_address = db.Column(db.String(255))
    consignee_contact_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=True)
    consignee_phone = db.Column(db.String(255))
    declared = db.Column(db.Float, default=.0)
    desc = db.Column(db.Text, default="")
    point_from_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    point_to_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    shipper_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    shipper_address = db.Column(db.String(255))
    shipper_contact_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=True)
    shipper_phone = db.Column(db.String(255))

    attachments = db.relationship('Attachment', cascade='all, delete', lazy=True, backref="order")

    def __repr__(self) -> str:
        return f"<Cargo {self.title}, {self.id}>"

    def __str__(self) -> str:
        return f"Order #{self.id} of {datetime.strftime(self.create_date, '%Y-%m-%d')}"

    @property
    def weight(self):
        return sum([attachment.weight for attachment in self.attachments])

    @property
    def volume(self):
        return sum([attachment.volume for attachment in self.attachments])

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


class Attachment(db.Model, Attachment):
    weight = db.Column(db.Float)
    volume = db.Column(db.Float)
    height = db.Column(db.Float)
    width = db.Column(db.Float)
    depth = db.Column(db.Float)
    order_id = db.Column(db.Integer, db.ForeignKey(Order.id), nullable=True)

    def __repr__(self) -> str:
        return f"<Attachment {self.id} for order {self.order_id}>"

    def __str__(self) -> str:
        return f"{self.height}x{self.width}x{self.depth}"
