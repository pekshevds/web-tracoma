from webapp.db import IssuanceOfCargo
from webapp.db.issuance_of_cargo.models import AttachmentIssuanceOfCargo
from webapp.db.issuance_of_cargo.fetchers import get_attachment_by_id, get_issuance_by_id
from webapp.db.utils.crud_utils import update_or_create_item, delete_item, update_or_create_item_from_form


def update_or_create_attachment(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_attachment_by_id, new_object_class=AttachmentIssuanceOfCargo,
                                 **kwargs)


def delete_attachment(id: int):
    return delete_item(id=id, get_func=get_attachment_by_id)


def save_attachment(form):
    return update_or_create_item_from_form(form, get_attachment_by_id, AttachmentIssuanceOfCargo)


def update_or_create_receipt(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_issuance_by_id, new_object_class=IssuanceOfCargo, **kwargs)


def delete_receipt(id: int):
    return delete_item(id=id, get_func=get_issuance_by_id)


def save_receipt(form):
    return update_or_create_item_from_form(form, get_issuance_by_id, IssuanceOfCargo)
