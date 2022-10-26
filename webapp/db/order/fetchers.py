from webapp.db import Order
from webapp.db.order.models import Attachment


def get_orders():
    return Order.query.filter().all()


def get_order_by_id(id: int):
    try:
        return Order.query.get(id)
    except (RuntimeError):
        return None


def get_attachments(order_id: int):
    return Attachment.query.filter(Attachment.order_id == order_id).all()


def get_attachment_by_id(id: int):
    try:
        return Attachment.query.get(id)
    except (RuntimeError):
        return None
