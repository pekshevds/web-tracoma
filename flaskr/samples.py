from flaskr.models import Storage


def get_storages(storage_type=None) -> list:
    if storage_type:
        return Storage.query.filter_by(type=storage_type).all()
    else:
        return Storage.query.all()
    

def get_storage_by_id(id: int) -> Storage:
    try:
        storage = Storage.query.get(id)
    except:
        storage = None    
    return storage
