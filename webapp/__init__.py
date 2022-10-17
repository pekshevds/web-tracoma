from flask import Flask
from os.path import abspath
from webapp.db.models import db

from webapp.views import home_view, about_view
from webapp.views.point import delete_point_view, points_view, point_view, \
    new_point_view, save_point_view
from webapp.views.order import delete_order_view, orders_view, order_view, \
    new_order_view, save_order_view
from webapp.views.storage import storages_view, storages_by_kind_view, \
    storage_view, new_storage_view, delete_storage_view, save_storage_view


def create_app():
    
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + abspath('db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['CSRF_ENABLED'] = True
    app.config['SECRET_KEY'] = "test_secret_key"

    db.init_app(app)

    app.add_url_rule("/", endpoint="home", view_func=home_view)
    app.add_url_rule("/home", endpoint="home", view_func=home_view)
    app.add_url_rule("/about", endpoint="about", view_func=about_view)
    
    #ORDERS
    app.add_url_rule("/orders", endpoint="orders", view_func=orders_view)
    app.add_url_rule("/orders/show/<int:order_id>", endpoint="show_order", view_func=order_view)
    app.add_url_rule("/orders/new", endpoint="new_order", view_func=new_order_view)
    app.add_url_rule("/orders/delete/<int:order_id>", endpoint="delete_order", view_func=delete_order_view)
    app.add_url_rule("/orders/save", endpoint="save_order", view_func=save_order_view, methods=['POST'])

    #STORAGES
    app.add_url_rule("/storages", endpoint="storages", view_func=storages_view)
    app.add_url_rule("/storages/kind/<int:storage_kind>", endpoint="storages_by_kind", view_func=storages_by_kind_view)
    app.add_url_rule("/storages/show/<int:storage_id>", endpoint="show_storage", view_func=storage_view)
    app.add_url_rule("/storages/new/<int:storage_kind>", endpoint="new_storage", view_func=new_storage_view)
    app.add_url_rule("/storages/delete/<int:storage_id>", endpoint="delete_storage", view_func=delete_storage_view)
    app.add_url_rule("/storages/save", endpoint="save_storage", view_func=save_storage_view, methods=['POST'])
    
    #POINTS
    app.add_url_rule("/points", endpoint="points", view_func=points_view)
    app.add_url_rule("/points/show/<int:point_id>", endpoint="show_point", view_func=point_view)
    app.add_url_rule("/points/new", endpoint="new_point", view_func=new_point_view)
    app.add_url_rule("/points/delete/<int:point_id>", endpoint="delete_point", view_func=delete_point_view)
    app.add_url_rule("/points/save", endpoint="save_point", view_func=save_point_view, methods=['POST'])
            
    return app
