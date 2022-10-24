from webapp.db import Order


def get_orders():
    return Order.query.filter().all()


def get_order_by_id(id: int):
    try:
        return Order.query.get(id)
    except (RuntimeError):
        return None
