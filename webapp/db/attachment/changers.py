from webapp.db import Attachment
from webapp.db.attachment.fetchers import get_attachment_by_id
from webapp.db.utils.crud_utils import update_or_create_item, delete_item, update_or_create_item_from_form


def update_or_create_attachment(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_attachment_by_id, new_object_class=Attachment, **kwargs)


def delete_attachment(id: int):
    return delete_item(id=id, get_func=get_attachment_by_id)


def save_attachment(form):
    return update_or_create_item_from_form(form, get_attachment_by_id, Attachment)
