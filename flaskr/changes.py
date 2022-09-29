from flask_sqlalchemy import SQLAlchemy
from flaskr.models import Storage


db = SQLAlchemy()


def delete_storage_by_id(id: int):
    storage = Storage.query.get(id)
    db.session.delete(storage)
    db.session.commit()


def add_storage(title:str, inn: str, type:int=1):    
    storage = Storage(title=title, inn=inn, type=type)
    db.session.add(storage)
    db.session.commit()


def update_storage(id:int, title:str, inn: str, type:int=1):
    storage = Storage.query.get(id)
    storage.title = title
    storage.inn = inn
    storage.type = type
    db.session.add(storage)
    db.session.commit()
