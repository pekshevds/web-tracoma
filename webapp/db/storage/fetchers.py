from webapp.db.models import Storage

def get_storages():
    return Storage.query.filter(Storage.is_mark==False).all()


def get_storages_by_kind(kind: int):
    return Storage.query.filter(Storage.is_mark==False, Storage.kind==kind).all()


def get_storage_by_id(storage_id: int):
    return Storage.query.get(storage_id)
    