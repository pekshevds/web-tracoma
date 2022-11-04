from webapp.db import Order
from webapp.db.order.models import Attachment


def get_orders():
    return Order.query.filter().all()


def get_order_by_id(id: int):
    return Order.query.filter(Order.id == id).first()


def get_attachments(order_id: int):
    return Attachment.query.filter(Attachment.order_id == order_id).all()


def get_attachment_by_id(id: int):
    return Attachment.query.filter(Attachment.id == id).first()
