import imp
from flask import Flask
from flask_migrate import Migrate
from os.path import abspath
from webapp.db.common import db
from webapp.urls.common import add_urls
from webapp.urls.point_urls import get_point_blueprints


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

    return app
