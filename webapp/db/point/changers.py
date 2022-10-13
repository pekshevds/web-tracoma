from webapp.db.models import Point, db
from webapp.db.point.fetchers import get_point_by_id


from webapp.db.crud_utils import update_or_create_item, delete_item


def update_or_create_point(id: int, **kwargs):
    return update_or_create_item(id=id, db=db, get_func=get_point_by_id, Object=Point, kwargs=kwargs)


def delete_point(id: int):
    return delete_item(id=id, db=db, get_func=get_point_by_id)
    
