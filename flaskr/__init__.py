from flask import Flask
import os
from flask import render_template, request, redirect, url_for
from flaskr.models import Storage, db
from db import delete_storage_by_id, get_storages, add_storage, \
    update_storage, get_storage_by_id


def navigation_roates(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/storages')
    def storages():
        return render_template('storage_list.html', storages=get_storages())

def storage_roates(app):
    @app.route('/new-storage')
    def new_storage():
        return render_template('storage_item.html', storage=None)

    @app.route('/delete-storage/<int:storage_id>')
    def delete_storage(storage_id):        
        delete_storage_by_id(app, storage_id)
        return redirect(url_for('storages'))

    @app.route('/storage/<int:storage_id>')
    def show_storage(storage_id):        
        return render_template('storage_item.html', storage=get_storage_by_id(storage_id))

    @app.route('/save_storage', methods=['POST', 'PUT'])
    def save_storage():
        
        id = request.values.get('id', '')
        title = request.values.get('title', '')
        inn = request.values.get('inn', '')
        if id == '':
            add_storage(app, title=title, inn=inn)
        else:
            update_storage(app, int(id), title=title, inn=inn)

        return redirect(url_for('storages'))

def create_app():
    
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath('db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    navigation_roates(app)
    storage_roates(app)
    
    return app