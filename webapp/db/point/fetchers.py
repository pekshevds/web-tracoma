from webapp.db.models import Point

def get_points():
    return Point.query.filter(Point.is_mark==False).all()


def get_point_by_id(point_id: int):
    return Point.query.get(point_id)
    