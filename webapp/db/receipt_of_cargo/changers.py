from webapp.db import ReceiptOfCargo
from webapp.db.receipt_of_cargo.models import AttachmentReceiptOfCargo
from webapp.db.receipt_of_cargo.fetchers import get_attachment_by_id, get_receipt_by_id
from webapp.db.utils.crud_utils import update_or_create_item, delete_item, update_or_create_item_from_form


def update_or_create_attachment(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_attachment_by_id, new_object_class=AttachmentReceiptOfCargo,
                                 **kwargs)


def delete_attachment(id: int):
    return delete_item(id=id, get_func=get_attachment_by_id)


def save_attachment(form):
    return update_or_create_item_from_form(form, get_attachment_by_id, AttachmentReceiptOfCargo)


def update_or_create_receipt(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_receipt_by_id, new_object_class=ReceiptOfCargo, **kwargs)


def delete_receipt(id: int):
    return delete_item(id=id, get_func=get_receipt_by_id)


def save_receipt(form):
    return update_or_create_item_from_form(form, get_receipt_by_id, ReceiptOfCargo)
