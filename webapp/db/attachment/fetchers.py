from webapp.db import Attachment


def get_attachments(order_id: int):
    return Attachment.query.filter(Attachment.order_id == order_id).all()


def get_attachment_by_id(id: int):
    try:
        return Attachment.query.get(id)
    except (RuntimeError):
        return None
