from webapp.db import CargoMovement
from webapp.db.cargo_movement.models import AttachmentCargoMovement
from webapp.db.cargo_movement.fetchers import get_attachment_by_id, get_movement_by_id
from webapp.db.utils.crud_utils import update_or_create_item, delete_item, update_or_create_item_from_form


def update_or_create_attachment(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_attachment_by_id, new_object_class=AttachmentCargoMovement,
                                 **kwargs)


def delete_attachment(id: int):
    return delete_item(id=id, get_func=get_attachment_by_id)


def save_attachment(form):
    return update_or_create_item_from_form(form, get_attachment_by_id, AttachmentCargoMovement)


def update_or_create_movement(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_movement_by_id, new_object_class=CargoMovement, **kwargs)


def delete_movement(id: int):
    return delete_item(id=id, get_func=get_movement_by_id)


def save_movement(form):
    return update_or_create_item_from_form(form, get_movement_by_id, CargoMovement)
