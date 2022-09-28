from flask import Flask
from flask import render_template


def create_app():
    app = Flask(__name__, static_url_path='/static')

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app