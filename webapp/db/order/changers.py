from webapp.db import Order
from webapp.db.order.fetchers import get_order_by_id
from webapp.db.utils.crud_utils import update_or_create_item, delete_item, update_or_create_item_from_form


def update_or_create_order(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_order_by_id, new_object_class=Order, **kwargs)


def delete_order(id: int):
    return delete_item(id=id, get_func=get_order_by_id)

def save_order(form):
    return update_or_create_item_from_form(form, get_order_by_id, Order)
