from webapp.db import Point


def get_points():
    return Point.query.filter().all()


def get_point_by_id(id: int):
    return Point.query.filter(Point.id == id).first()
