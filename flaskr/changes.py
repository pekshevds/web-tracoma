from flaskr.models import Storage, Point, db


def delete_storage_by_id(id: int) -> bool:
    try:
        storage = Storage.query.get(id)
        storage.is_mark = True
        db.session.add(storage)
        db.session.commit()
    except:
        return False
    return True


def add_storage(title: str='', inn: str='', \
                is_internal: bool=False, is_employee: bool=False, \
                kpp: str='', weight: float=.0, volume: float=.0, \
                kind: int=1) -> bool:
    try:
        storage = Storage(title=title, inn=inn, kind=kind, \
                            is_internal=is_internal, is_employee=is_employee, \
                            kpp=kpp, weight=weight, volume=volume, is_mark=False)
        db.session.add(storage)
        db.session.commit()
    except:
        return False
    return True


def update_storage(id: int, title: str='', inn: str='', \
                    is_internal: bool=False, is_employee: bool=False, \
                    kpp: str='', weight: float=.0, volume: float=.0, \
                    kind: int=1) -> bool:
    try:        
        storage = Storage.query.get(id)
        storage.title = title
        storage.inn = inn
        storage.is_internal = is_internal
        storage.is_employee = is_employee
        storage.kpp = kpp
        storage.weight = weight
        storage.volume = volume
        storage.kind = kind
        db.session.add(storage)
        db.session.commit()
    except:
        return False
    return True


def delete_point_by_id(id: int) -> bool:
    try:
        point = Point.query.get(id)
        point.is_mark = True
        db.session.add(point)
        db.session.commit()
    except:
        return False
    return True


def add_point(title: str='', short: str='') -> bool:
    try:
        point = Point(title=title, short=short, is_mark=False)
        db.session.add(point)
        db.session.commit()
    except:
        return False
    return True


def update_point(id: int, title: str='', short: str='') -> bool:
    try:        
        point = Point.query.get(id)
        point.title = title
        point.short = short        
        db.session.add(point)
        db.session.commit()
    except:
        return False
    return True
