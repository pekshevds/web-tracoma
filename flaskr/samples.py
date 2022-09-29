from flaskr.models import Storage


def get_storages():    
    return Storage.query.all()


def get_storage_by_id(id: int):
    return Storage.query.get(id)
