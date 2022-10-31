from webapp.db import ReceiptOfCargo
from webapp.db.receipt_of_cargo.models import AttachmentReceiptOfCargo


def get_receipts():
    return ReceiptOfCargo.query.filter().all()


def get_receipt_by_id(id: int):
    try:
        return ReceiptOfCargo.query.get(id)
    except (RuntimeError):
        return None


def get_attachments(receipt_id: int):
    return AttachmentReceiptOfCargo.query.filter(AttachmentReceiptOfCargo.receipt_id == receipt_id).all()


def get_attachment_by_id(id: int):
    try:
        return AttachmentReceiptOfCargo.query.get(id)
    except (RuntimeError):
        return None
