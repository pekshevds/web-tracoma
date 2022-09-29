from flask import Flask
from os.path import abspath
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flaskr.views import get_home_view, get_about_view, get_storages_view, \
    get_new_storage_view, get_storeges_after_deleting_by_id, get_storage_view, \
        get_storeges_after_create_update_by_id


db = SQLAlchemy()


def navigation_routes(app):
    @app.route('/')
    @app.route('/index')
    def home():
        return get_home_view()


    @app.route('/about')
    def about():
        return get_about_view()


    @app.route('/storages')
    def storages():
        return get_storages_view()


def storage_routes(app):
    @app.route('/new-storage')
    def new_storage():
        return get_new_storage_view()


    @app.route('/delete-storage/<int:storage_id>')
    def delete_storage(storage_id):        
        return get_storeges_after_deleting_by_id(storage_id)


    @app.route('/storage/<int:storage_id>')
    def show_storage(storage_id):        
        return get_storage_view(storage_id)


    @app.route('/save_storage', methods=['POST', 'PUT'])
    def save_storage():
        
        id = request.values.get('id', '')
        title = request.values.get('title', '')
        inn = request.values.get('inn', '')
        return get_storeges_after_create_update_by_id(storage_id=id, title=title, inn=inn)


def create_app():
    
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + abspath('db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    navigation_routes(app)
    storage_routes(app)
    
    return app
