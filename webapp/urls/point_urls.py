from flask.blueprints import Blueprint
from webapp.views.point import PointView


def get_point_blueprints():
    point = Blueprint(name='point', import_name='point', url_prefix='/points')
    point.add_url_rule('/', endpoint='points', view_func=PointView.points_view)
    point.add_url_rule('/show/<int:point_id>', endpoint='show_point', view_func=PointView.as_view('show_point'))
    point.add_url_rule('/new', endpoint='new_point', view_func=PointView.as_view('new_point'))
    point.add_url_rule('/delete/<int:point_id>', endpoint='delete_point', view_func=PointView.delete_point_view)
    point.add_url_rule('/save', view_func=PointView.as_view('save_point'))
    return point
