from flaskr.models import Storage


def get_storages(storage_kind=None) -> list:
    if storage_kind:
        return Storage.query.filter_by(kind=storage_kind).all()
    else:
        return Storage.query.all()
    

def get_storage_by_id(id: int) -> Storage:
    try:
        storage = Storage.query.get(id)
    except:
        storage = None    
    return storage
