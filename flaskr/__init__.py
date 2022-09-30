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
        return get_storages_view(storage_type=None)
        
    @app.route('/storages/type')
    @app.route('/storages/type/<int:storage_type>')
    def storages_by_type(storage_type=None):
        return get_storages_view(storage_type)


def storage_routes(app):
    @app.route('/new-storage')
    def new_storage():
        return get_new_storage_view()


    @app.route('/delete-storage/<int:storage_id>')
    def delete_storage(storage_id):
        return get_storeges_after_deleting_by_id(storage_id=storage_id)


    @app.route('/storage/<int:storage_id>')
    def show_storage(storage_id):
        return get_storage_view(storage_id)


    @app.route('/save_storage', methods=['POST', 'PUT'])
    def save_storage():        
        
        try:
            id = int(request.values.get('id', '0'))
        except:
            id = 0
        title = request.values.get('title', '')
        inn = request.values.get('inn', '')
        
        is_internal = request.values.get('is_internal')        
        if is_internal:
            is_internal = bool(is_internal)
        else:
            is_internal = False

        is_employee = request.values.get('is_employee')
        if is_employee:
            is_employee = bool(is_employee)
        else:
            is_employee = False

        kpp = request.values.get('kpp', '')

        try:
            weight = request.values.get('weight', '0')
        except:
            weight = 0
        try:
            volume = request.values.get('volume', '0')
        except:
            volume = 0
        
        try:
            type = int(request.values.get('type', '1'))
        except:
            type = 1
        return get_storeges_after_create_update_by_id(storage_id=id, title=title, inn=inn, \
            is_internal=is_internal, is_employee=is_employee, kpp=kpp, weight=weight,\
                volume=volume, type=type)


def create_app():
    
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + abspath('db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    navigation_routes(app)
    storage_routes(app)
    
    return app
