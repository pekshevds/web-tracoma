from webapp.db.common import db, Directory, Attachment
from webapp.db import Order, Storage
from webapp.db.storage.fetchers import get_storage_by_id
from webapp.db.order.fetchers import get_order_by_id
from datetime import datetime


class CargoMovement(db.Model, Directory):
    shipper_id = db.Column(db.Integer, db.ForeignKey(Storage.id), nullable=True)
    consignee_id = db.Column(db.Integer, db.ForeignKey(Storage.id), nullable=True)
    cost = db.Column(db.Float, default=.0)
    attachments = db.relationship('AttachmentCargoMovement', cascade='all, delete', lazy=True, backref="movement")

    def __repr__(self) -> str:
        return f"<CargoMovement {self.title}, {self.id}>"

    def __str__(self) -> str:
        return f"Cargo movement #{self.id} of {datetime.strftime(self.create_date, '%Y-%m-%d')}"

    @property
    def shipper(self):
        return get_storage_by_id(id=self.shipper_id)

    @property
    def consignee(self):
        return get_storage_by_id(id=self.consignee_id)

    @property
    def weight(self):
        return sum([attachment.order.weight for attachment in self.attachments])

    @property
    def volume(self):
        return sum([attachment.order.volume for attachment in self.attachments])


class AttachmentCargoMovement(db.Model, Attachment):
    movement_id = db.Column(db.Integer, db.ForeignKey(CargoMovement.id), nullable=True)
    order_id = db.Column(db.Integer, db.ForeignKey(Order.id), nullable=True)

    def __repr__(self) -> str:
        return f"<Attachment movement {self.id}>"

    @property
    def order(self):
        return get_order_by_id(id=self.order_id)
