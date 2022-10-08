from webapp.db.models import Storage, db
from webapp.db.storage.fetchers import get_storage_by_id
from sqlalchemy.exc import SQLAlchemyError


def update_or_create_storage(storage_id: int, **kwargs):
    storage = get_storage_by_id(storage_id=storage_id)
    if not storage:
        storage = Storage()

    for item in kwargs.items():
        if hasattr(storage, item[0]):
            setattr(storage, item[0], item[1])
    try:
        db.session.add(storage)
        db.session.commit()
    except SQLAlchemyError:
        return False
    return True


def delete_storage(storage_id: int):
    storage = get_storage_by_id(storage_id=storage_id)
    if storage:
        storage.is_mark = True
        try:
            db.session.add(storage)
            db.session.commit()
        except SQLAlchemyError:
            return False
    return True
