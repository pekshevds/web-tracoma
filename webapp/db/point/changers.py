from webapp.db import Point
from webapp.db.point.fetchers import get_point_by_id
from webapp.db.utils.crud_utils import update_or_create_item, delete_item


def update_or_create_point(id: int, **kwargs):
    return update_or_create_item(id=id, get_func=get_point_by_id, new_object_class=Point, **kwargs)


def delete_point(id: int):
    return delete_item(id=id, get_func=get_point_by_id)
    
