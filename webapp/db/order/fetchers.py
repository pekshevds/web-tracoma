from webapp.db.models import Order

def get_orders():
    return Order.query.filter(Order.is_deleted==False).all()


def get_order_by_id(id: int):
    try:
        return Order.query.get(id)
    except:
        return None
