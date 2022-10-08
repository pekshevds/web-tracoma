from webapp.db.models import Point, db
from webapp.db.point.fetchers import get_point_by_id
from sqlalchemy.exc import SQLAlchemyError


def update_or_create_point(point_id: int, **kwargs):
    point = get_point_by_id(point_id=point_id)
    if not point:
        point = Point()

    for item in kwargs.items():
        if hasattr(point, item[0]):
            setattr(point, item[0], item[1])
    try:
        db.session.add(point)
        db.session.commit()
    except SQLAlchemyError:
        return False
    return True


def delete_point(point_id: int):
    point = get_point_by_id(point_id=point_id)
    if point:
        point.is_mark = True
        try:
            db.session.add(point)
            db.session.commit()
        except SQLAlchemyError:
            return False
    return True
