from webapp.db.models import Storage


def get_storages():
    return Storage.query.filter(Storage.is_deleted==False).all()

def get_storages_by_kind(kind: int):
    return Storage.query.filter(
        Storage.is_deleted==False, 
        Storage.kind==kind).all()

def get_storage_by_id(id: int):
    return Storage.query.get(id)

def get_carriers():
    return Storage.query.filter(
        Storage.is_deleted==False, 
        Storage.is_internal==True).all()

def get_counteragents():
    return Storage.query.filter(
        Storage.is_deleted==False, 
        Storage.is_internal==False, 
        Storage.is_employee==False).all()
