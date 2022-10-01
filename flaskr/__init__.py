from flask import Flask
from os.path import abspath
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flaskr.views import get_home_view, get_about_view
from flaskr.views_storages import get_storages_view, \
    get_new_storage_view, get_storeges_after_deleting_by_id, get_storage_view, \
    get_storeges_after_create_update_by_id
from flaskr.views_points import get_points_view, get_new_point_view, get_points_after_deleting_by_id, \
    get_point_view, get_points_after_create_update_by_id


from flaskr.utils import validate_paramas_for_storage

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
        return get_storages_view(storage_kind=None)
        
    @app.route('/storages/kind')
    @app.route('/storages/kind/<int:storage_kind>')
    def storages_by_kind(storage_kind=None):
        return get_storages_view(storage_kind)

    @app.route('/points')
    def points():
        return get_points_view()


def storage_routes(app):
    @app.route('/new-storage/<int:storage_kind>')
    def new_storage(storage_kind=1):
        return get_new_storage_view(storage_kind)


    @app.route('/delete-storage/<int:storage_id>')
    def delete_storage(storage_id):
        return get_storeges_after_deleting_by_id(storage_id=storage_id)


    @app.route('/storage/<int:storage_id>')
    def show_storage(storage_id):
        return get_storage_view(storage_id)


    @app.route('/save_storage', methods=['POST', 'PUT'])
    def save_storage():        
        
        id, title, inn, is_internal, is_employee, \
        kpp, weight, volume, kind = validate_paramas_for_storage(id=request.values.get('id'), title=request.values.get('title'), \
                                    inn=request.values.get('inn'), is_internal=request.values.get('is_internal'), \
                                    is_employee=request.values.get('is_employee'), kpp=request.values.get('kpp'), \
                                    weight=request.values.get('weight'), volume=request.values.get('volume'), \
                                    kind=request.values.get('kind'))        
        
        return get_storeges_after_create_update_by_id(storage_id=id, title=title, inn=inn, \
            is_internal=is_internal, is_employee=is_employee, kpp=kpp, weight=weight,\
                volume=volume, kind=kind)


def point_routes(app):
    @app.route('/new-point')
    def new_point():
        return get_new_point_view()


    @app.route('/delete-point/<int:point_id>')
    def delete_point(point_id):
        return get_points_after_deleting_by_id(point_id=point_id)


    @app.route('/point/<int:point_id>')
    def show_point(point_id):
        return get_point_view(point_id)


    @app.route('/save_point', methods=['POST', 'PUT'])
    def save_point():        
        id=request.values.get('id')
        title=request.values.get('title')
        short=request.values.get('short')
        return get_points_after_create_update_by_id(point_id=id, title=title, short=short)


def create_app():
    
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + abspath('db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    navigation_routes(app)
    storage_routes(app)
    point_routes(app)
    
    return app
