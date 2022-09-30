from flaskr.models import Storage, db


def delete_storage_by_id(id: int) -> bool:
    try:
        storage = Storage.query.get(id)
        db.session.delete(storage)
        db.session.commit()
    except:
        return False
    return True


def add_storage(title: str='', inn: str='', \
                is_internal: bool=False, is_employee: bool=False, \
                kpp: str='', weight: float=.0, volume: float=.0, \
                type: int=1) -> bool:
    try:
        storage = Storage(title=title, inn=inn, type=type, \
                            is_internal=is_internal, is_employee=is_employee, \
                            kpp=kpp, weight=weight, volume=volume)
        db.session.add(storage)
        db.session.commit()
    except:
        return False
    return True


def update_storage(id: int, title: str='', inn: str='', \
                    is_internal: bool=False, is_employee: bool=False, \
                    kpp: str='', weight: float=.0, volume: float=.0, \
                    type: int=1) -> bool:
    try:        
        storage = Storage.query.get(id)
        storage.title = title
        storage.inn = inn
        storage.is_internal = is_internal
        storage.is_employee = is_employee
        storage.kpp = kpp
        storage.weight = weight
        storage.volume = volume
        storage.type = type
        db.session.add(storage)
        db.session.commit()
    except:
        return False
    return True
