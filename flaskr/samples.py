from flaskr.models import Storage, Point


def get_storages(storage_kind=None) -> list:
    if storage_kind:
        return Storage.query.filter_by(kind=storage_kind, is_mark=False).all()
    else:
        return Storage.query.filter_by(is_mark=False).all()
    

def get_storage_by_id(id: int) -> Storage:
    try:
        storage = Storage.query.get(id)
    except:
        storage = None    
    return storage


def get_points() -> list:
    return Point.query.filter_by(is_mark=False).all()


def get_point_by_id(id: int) -> Point:
    try:
        point = Point.query.get(id)
    except:
        point = None    
    return point