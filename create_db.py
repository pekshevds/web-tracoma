from flaskr import create_app
from flaskr.models import db


db.create_all(app=create_app())