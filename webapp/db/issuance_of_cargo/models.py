from webapp.db.common import db, Directory, Attachment
from webapp.db import Order, Storage
from webapp.db.storage.fetchers import get_storage_by_id
from webapp.db.order.fetchers import get_order_by_id
from datetime import datetime


class IssuanceOfCargo(db.Model, Directory):
    storage_id = db.Column(db.Integer, db.ForeignKey(Storage.id), nullable=True)
    cost = db.Column(db.Float, default=.0)
    attachments = db.relationship('AttachmentIssuanceOfCargo', cascade='all, delete', lazy=True, backref="issuance")

    def __repr__(self) -> str:
        return f"<IssuanceOfCargo {self.title}, {self.id}>"

    def __str__(self) -> str:
        return f"Issuance of cargo #{self.id} of {datetime.strftime(self.create_date, '%Y-%m-%d')}"

    @property
    def storage(self):
        return get_storage_by_id(id=self.storage_id)

    @property
    def weight(self):
        return sum([attachment.order.weight for attachment in self.attachments])

    @property
    def volume(self):
        return sum([attachment.order.volume for attachment in self.attachments])


class AttachmentIssuanceOfCargo(db.Model, Attachment):
    issuance_id = db.Column(db.Integer, db.ForeignKey(IssuanceOfCargo.id), nullable=True)
    order_id = db.Column(db.Integer, db.ForeignKey(Order.id), nullable=True)

    def __repr__(self) -> str:
        return f"<Attachment issuance {self.id}>"

    @property
    def order(self):
        return get_order_by_id(id=self.order_id)
