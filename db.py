from flaskr.models import db, Storage

def get_storages():    
    return Storage.query.all()

def get_storage_by_id(id: int):
    return Storage.query.get(id)

def delete_storage_by_id(app, id: int):
    with app.app_context():
        storage = Storage.query.get(id)
        db.session.delete(storage)
        db.session.commit()

def add_storage(app, title:str, inn: str, type:int=1):
    with app.app_context():
        storage = Storage(title=title, inn=inn, type=type)
        db.session.add(storage)
        db.session.commit()

def update_storage(app, id:int, title:str, inn: str, type:int=1):
    with app.app_context():
        storage = Storage.query.get(id)
        storage.title = title
        storage.inn = inn
        storage.type = type
        db.session.add(storage)
        db.session.commit()