from flaskr import create_app
from flaskr.models import db


app = create_app()
db.create_all(app=app)
