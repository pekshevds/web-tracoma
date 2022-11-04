from webapp.db import Route


def get_routes():
    return Route.query.filter().all()


def get_route_by_id(id: int):
    return Route.query.filter(Route.id == id).first()


def get_route_by_points(point_a_id: int, point_b_id: int):
    return Route.query.filter(Route.point_a_id == point_a_id, Route.point_b_id == point_b_id).first()
