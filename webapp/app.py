import imp
from flask import Flask
from flask_migrate import Migrate
from os.path import abspath
from webapp.db.common import db
from webapp.urls.common import add_urls
from webapp.urls.point_urls import get_point_blueprints
from webapp.urls.storage_urls import get_storage_blueprints
from webapp.urls.order_urls import get_order_blueprints
from webapp.urls.receipt_urls import get_receipt_blueprints
from webapp.urls.movement_urls import get_movement_blueprints


def create_app():

    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + abspath('db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['CSRF_ENABLED'] = True
    app.config['SECRET_KEY'] = "test_secret_key"
    db.init_app(app)

    migrate = Migrate(app, db, render_as_batch=True)
    add_urls(app)
    app.register_blueprint(get_point_blueprints())
    app.register_blueprint(get_storage_blueprints())
    app.register_blueprint(get_order_blueprints())
    app.register_blueprint(get_receipt_blueprints())
    app.register_blueprint(get_movement_blueprints())

    return app
