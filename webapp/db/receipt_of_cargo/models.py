from webapp.db.common import db, Directory, Attachment
from webapp.db import Order, Storage
from datetime import datetime


class ReceiptOfCargo(db.Model, Directory):
    storage_id = db.Column(db.Integer, db.ForeignKey(Storage.id), nullable=True)
    total = db.Column(db.Float, default=.0)
    attachments = db.relationship('AttachmentReceiptOfCargo', cascade='all, delete', lazy=True)

    def __repr__(self) -> str:
        return f"<ReceiptOfCargo {self.title}, {self.id}>"

    def __str__(self) -> str:
        return f"Receipt of cargo #{self.id} of {datetime.strftime(self.create_date, '%Y-%m-%d')}"


class AttachmentReceiptOfCargo(db.Model, Attachment):
    receipt_id = db.Column(db.Integer, db.ForeignKey(ReceiptOfCargo.id), nullable=True)
    order_id = db.Column(db.Integer, db.ForeignKey(Order.id), nullable=True)

    def __repr__(self) -> str:
        return f"<Attachment receipt {self.id}>"
