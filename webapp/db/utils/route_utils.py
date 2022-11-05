import json
from sqlalchemy.exc import SQLAlchemyError
from webapp.db.point.fetchers import get_point_by_name, get_points
from webapp.db.route.fetchers import get_route_by_points
from webapp.db.common import db
from webapp.db.point.models import Point
from webapp.db.route.models import Route

from geopy.exc import GeocoderTimedOut, GeocoderQueryError, GeocoderUnavailable
from geopy.distance import geodesic
from geopy.geocoders import Nominatim


def fetch_city_location(city_name: str):
    geolocator = Nominatim(user_agent=__name__)
    try:
        location = geolocator.geocode(city_name.lower())
    except (GeocoderTimedOut, GeocoderQueryError, GeocoderUnavailable):
        return False
    return location


def fetch_distance_between_cities(point_a: dict, point_b: dict) -> int:
    try:
        distance = round(geodesic(point_a, point_b).km)
    except (GeocoderTimedOut, GeocoderQueryError, GeocoderUnavailable):
        distance = 0
    return distance


def fetch_cities_from_file():
    cities = []
    with open('webapp/static/cities.json', mode='r', encoding='utf-8') as fp:
        for item in json.load(fp):
            cities.append(item['city'])
    return cities


def fetch_new_points_by_city_name(cities: list):
    new_points = []
    for city_name in cities:
        point = get_point_by_name(city_name)
        if not point:
            point = Point(title=city_name)
            location = fetch_city_location(city_name=city_name)
            if location:
                point.latitude = location.latitude
                point.longitude = location.longitude
            new_points.append(point)
    return new_points


def point_list_update() -> bool:
    cities = fetch_cities_from_file()
    new_points = fetch_new_points_by_city_name(cities)

    db.session.bulk_save_objects(new_points)
    try:
        db.session.commit()
    except (RuntimeError, SQLAlchemyError):
        return False
    return True


def routes_update() -> bool:
    new_routes = []
    points = get_points()
    for point_a in points:
        for point_b in points[::-1]:
            if point_a is point_b:
                break
            route = get_route_by_points(point_a.id, point_b.id)
            if not route:
                route = Route(point_a_id=point_a.id, point_b_id=point_b.id)
                route.distance = fetch_distance_between_cities(point_a.location, point_b.location)
                new_routes.append(route)
    db.session.bulk_save_objects(new_routes)
    try:
        db.session.commit()
    except (RuntimeError, SQLAlchemyError):
        return False
    return True


if __name__ == "__main__":
    routes_update()
