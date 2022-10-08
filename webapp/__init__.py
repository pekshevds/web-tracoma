from flask import Flask
from os.path import abspath
from webapp.db.models import db

from webapp.views import home_view, about_view
from webapp.views.point.views import delete_point_view, points_view, point_view, \
    new_point_view, save_point_view
from webapp.views.storage.views import storages_view, storages_by_kind_view, \
    storage_view, new_storage_view, delete_storage_view, save_storage_view


def create_app():
    
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + abspath('db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.add_url_rule("/", endpoint="home", view_func=home_view)
    app.add_url_rule("/home", endpoint="home", view_func=home_view)
    app.add_url_rule("/about", endpoint="about", view_func=about_view)
    
    #STORAGES
    app.add_url_rule("/storages", endpoint="storages", view_func=storages_view)
    app.add_url_rule("/storages/kind/<int:storage_kind>", endpoint="storages_by_kind", view_func=storages_by_kind_view)
    app.add_url_rule("/storage/show/<int:storage_id>", endpoint="show_storage", view_func=storage_view)
    app.add_url_rule("/storage/new/<int:storage_kind>", endpoint="new_storage", view_func=new_storage_view)
    app.add_url_rule("/storage/delete/<int:storage_id>", endpoint="delete_storage", view_func=delete_storage_view)
    app.add_url_rule("/storage/save", endpoint="save_storage", view_func=save_storage_view, methods=['POST', 'PUT'])
    
    #POINTS
    app.add_url_rule("/points", endpoint="points", view_func=points_view)
    app.add_url_rule("/point/show/<int:point_id>", endpoint="show_point", view_func=point_view)
    app.add_url_rule("/point/new", endpoint="new_point", view_func=new_point_view)
    app.add_url_rule("/point/delete/<int:point_id>", endpoint="delete_point", view_func=delete_point_view)
    app.add_url_rule("/point/save", endpoint="save_point", view_func=save_point_view, methods=['POST', 'PUT'])
            
    return app
