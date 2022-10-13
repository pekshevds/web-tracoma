from webapp.db.models import Point

def get_points():
    return Point.query.filter(Point.is_deleted==False).all()


def get_point_by_id(id: int):
    return Point.query.get(id)
    