from webapp.app import create_app
from webapp.db.common import db


app = create_app()
db.create_all(app=app)
