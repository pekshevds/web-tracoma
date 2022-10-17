from webapp.db.models import Order, db
from webapp.db.order.fetchers import get_order_by_id


from webapp.db.crud_utils import update_or_create_item, delete_item


def update_or_create_order(id: int, **kwargs):
    return update_or_create_item(id=id, db=db, get_func=get_order_by_id, object=Order, **kwargs)


def delete_order(id: int):
    return delete_item(id=id, db=db, get_func=get_order_by_id)
    
