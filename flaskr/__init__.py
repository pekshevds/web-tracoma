from flask import Flask
from flask import render_template, request
from flaskr.models import db
from flaskr.db import get_storages, add_storage, update_storage


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/storage', methods=['GET', 'POST'])
    def storage():
        if request.method == 'GET':
            return render_template('storage_item.html')

        id = int(request.values.get('id', 0))
        title = request.values.get('title', '')
        inn = request.values.get('inn', '')
        if id == 0:
            add_storage(title=title)
        else:
            update_storage(id, title=title)    

        return render_template('storage_item.html')

    @app.route('/storages')
    def storages():
        return render_template('storage_list.html', storages=get_storages())        

    
    return app