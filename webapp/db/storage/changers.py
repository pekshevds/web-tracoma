from webapp.db import Storage
from webapp.db.storage.fetchers import get_storage_by_id
from webapp.db.utils.crud_utils import update_or_create_item, delete_item, update_or_create_item_from_form


def update_or_create_storage(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_storage_by_id, new_object_class=Storage, **kwargs)


def delete_storage(id: int):
    return delete_item(id=id, get_func=get_storage_by_id)

def save_storage(form):
    return update_or_create_item_from_form(form, get_storage_by_id, Storage)
