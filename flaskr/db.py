from flaskr.models import db, Storage


def get_storages():
    return Storage.query.all()

def add_storage(title:str, type:int=1):
    
    storage = Storage(title=title,type=type)
    db.session.add(storage)
    db.session.commit()

def update_storage(id:int, title:str, type:int=1):
    
    storage = Storage.query.get(id)
    storage.title = title
    db.session.add(storage)
    db.session.commit()