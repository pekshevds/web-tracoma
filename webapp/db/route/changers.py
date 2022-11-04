from webapp.db import Route
from webapp.db.route.fetchers import get_route_by_id
from webapp.db.utils.crud_utils import update_or_create_item, delete_item, update_or_create_item_from_form


def update_or_create_route(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_route_by_id, new_object_class=Route, **kwargs)


def delete_route(id: int):
    return delete_item(id=id, get_func=get_route_by_id)


def save_route(form):
    return update_or_create_item_from_form(form, get_route_by_id, Route)
