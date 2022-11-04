from flask.blueprints import Blueprint
from webapp.views.point import PointDetailView, PointListView, PointDeleteView


def get_point_blueprints():
    point = Blueprint(name='point', import_name='point', url_prefix='/points')
    point.add_url_rule('/', endpoint='points', view_func=PointListView.as_view('points'))
    point.add_url_rule('/show/<int:id>', endpoint='show_point', view_func=PointDetailView.as_view('show_point'))
    point.add_url_rule('/new', endpoint='new_point', view_func=PointDetailView.as_view('new_point'))
    point.add_url_rule('/delete/<int:id>', endpoint='delete_point', view_func=PointDeleteView.as_view('delete_point'))
    point.add_url_rule('/save', view_func=PointDetailView.as_view('save_point'))
    return point
