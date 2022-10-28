from flask import Flask
from os.path import abspath
from webapp.db.common import db

from webapp.views import home_view, about_view
from webapp.views.point import (delete_point_view, points_view, point_view,
                                new_point_view, save_point_view)
from webapp.views.order import (delete_order_view, orders_view, order_view,
                                new_order_view, save_order_view)
from webapp.views.order import (order_attachments_view, order_attachment_view,
                                order_new_attachment_view, order_save_attachment_view, order_delete_attachment_view)
from webapp.views.cargo_movement import (delete_movement_view, movements_view, movement_view,
                                         new_movement_view, save_movement_view,
                                         movement_attachments_view, movement_attachment_view,
                                         movement_new_attachment_view, movement_save_attachment_view,
                                         movement_delete_attachment_view)
from webapp.views.receipt_of_cargo import (delete_receipt_view, receipts_view, receipt_view,
                                           new_receipt_view, save_receipt_view,
                                           receipt_attachments_view, receipt_attachment_view,
                                           receipt_new_attachment_view, receipt_save_attachment_view,
                                           receipt_delete_attachment_view)
from webapp.views.storage import (storages_view, storages_by_kind_view,
                                  storage_view, new_storage_view, delete_storage_view, save_storage_view)


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

    # ORDERS
    prefix = "/orders"
    app.add_url_rule(f"{prefix}", endpoint="orders", view_func=orders_view)
    app.add_url_rule(f"{prefix}/show/<int:order_id>", endpoint="show_order", view_func=order_view)
    app.add_url_rule(f"{prefix}/new", endpoint="new_order", view_func=new_order_view)
    app.add_url_rule(f"{prefix}/delete/<int:order_id>", endpoint="delete_order", view_func=delete_order_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_order", view_func=save_order_view, methods=['POST'])
    app.add_url_rule(f"{prefix}/attachments/order/<int:order_id>", endpoint="order_attachments",
                     view_func=order_attachments_view)
    app.add_url_rule(f"{prefix}/attachments/show/<int:attachment_id>", endpoint="show_order_attachment",
                     view_func=order_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/new/order/<int:order_id>", endpoint="new_order_attachment",
                     view_func=order_new_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/delete/<int:attachment_id>", endpoint="delete_order_attachment",
                     view_func=order_delete_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/save", endpoint="save_order_attachment", methods=['POST'],
                     view_func=order_save_attachment_view)

    # RECEIP OF CARGO
    prefix = "/receipts"
    app.add_url_rule(f"{prefix}", endpoint="receipts", view_func=receipts_view)
    app.add_url_rule(f"{prefix}/show/<int:receipt_id>", endpoint="show_receipt", view_func=receipt_view)
    app.add_url_rule(f"{prefix}/new", endpoint="new_receipt", view_func=new_receipt_view)
    app.add_url_rule(f"{prefix}/delete/<int:receipt_id>", endpoint="delete_receipt", view_func=delete_receipt_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_receipt", view_func=save_receipt_view, methods=['POST'])
    app.add_url_rule(f"{prefix}/attachments/receipt/<int:receipt_id>", endpoint="receipt_attachments",
                     view_func=receipt_attachments_view)
    app.add_url_rule(f"{prefix}/attachments/show/<int:attachment_id>", endpoint="show_receipt_attachment",
                     view_func=receipt_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/new/receipt/<int:receipt_id>", endpoint="new_receipt_attachment",
                     view_func=receipt_new_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/delete/<int:attachment_id>", endpoint="delete_receipt_attachment",
                     view_func=receipt_delete_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/save", endpoint="save_receipt_attachment", methods=['POST'],
                     view_func=receipt_save_attachment_view)

    # CARGO MOVEMENT
    prefix = "/movements"
    app.add_url_rule(f"{prefix}", endpoint="movements", view_func=movements_view)
    app.add_url_rule(f"{prefix}/show/<int:movement_id>", endpoint="show_movement", view_func=movement_view)
    app.add_url_rule(f"{prefix}/new", endpoint="new_movement", view_func=new_movement_view)
    app.add_url_rule(f"{prefix}/delete/<int:movement_id>", endpoint="delete_movement", view_func=delete_movement_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_movement", view_func=save_movement_view, methods=['POST'])
    app.add_url_rule(f"{prefix}/attachments/movement/<int:movement_id>", endpoint="movement_attachments",
                     view_func=movement_attachments_view)
    app.add_url_rule(f"{prefix}/attachments/show/<int:attachment_id>", endpoint="show_movement_attachment",
                     view_func=movement_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/new/movement/<int:movement_id>", endpoint="new_movement_attachment",
                     view_func=movement_new_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/delete/<int:attachment_id>", endpoint="delete_movement_attachment",
                     view_func=movement_delete_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/save", endpoint="save_movement_attachment", methods=['POST'],
                     view_func=movement_save_attachment_view)

    # STORAGES
    prefix = "/storages"
    app.add_url_rule(f"{prefix}", endpoint="storages", view_func=storages_view)
    app.add_url_rule(f"{prefix}/kind/<int:storage_kind>", endpoint="storages_by_kind", view_func=storages_by_kind_view)
    app.add_url_rule(f"{prefix}/show/<int:storage_id>", endpoint="show_storage", view_func=storage_view)
    app.add_url_rule(f"{prefix}/new/<int:storage_kind>", endpoint="new_storage", view_func=new_storage_view)
    app.add_url_rule(f"{prefix}/delete/<int:storage_id>", endpoint="delete_storage", view_func=delete_storage_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_storage", view_func=save_storage_view, methods=['POST'])

    # POINTS
    prefix = "/points"
    app.add_url_rule(f"{prefix}", endpoint="points", view_func=points_view)
    app.add_url_rule(f"{prefix}/show/<int:point_id>", endpoint="show_point", view_func=point_view)
    app.add_url_rule(f"{prefix}/new", endpoint="new_point", view_func=new_point_view)
    app.add_url_rule(f"{prefix}/delete/<int:point_id>", endpoint="delete_point", view_func=delete_point_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_point", view_func=save_point_view, methods=['POST'])

    return app
