from typing import Callable, Type
from sqlalchemy.exc import SQLAlchemyError
from webapp.db.common import db


def fill_field_values(item, **kwargs):
    for key, value in kwargs.items():
        if hasattr(item, key):
            setattr(item, key, value)


def update_or_create_item(id: int, get_func: Callable, new_object_class: Type, **kwargs) -> bool:
    """
    updates an existing record in the database or creates a new record
    """

    item = get_func(id=id)
    if not item:
        item = new_object_class(**kwargs)
    else:
        fill_field_values(item, **kwargs)

    db.session.add(item)
    try:
        db.session.commit()
    except (RuntimeError, SQLAlchemyError):
        return False
    return True


def update_or_create_item_from_form(form, get_func: Callable, new_object_class: Type) -> bool:
    """
    updates an existing record in the database or creates a new record
    """

    id = form.id.data
    if id:
        new_object = get_func(id=id)
        form.populate_obj(new_object)
    else:
        new_object = new_object_class()
        form.populate_obj(new_object)
        new_object.id = new_object

    db.session.add(new_object)

    try:
        db.session.commit()
    except (RuntimeError, SQLAlchemyError):
        return False
    return True


def delete_item(id: int, get_func: Callable) -> bool:
    """
    marks a database record as deleted
    """
    item = get_func(id=id)
    if item:
        item.is_deleted = True
        db.session.add(item)
        try:
            db.session.commit()
        except SQLAlchemyError:
            return False
    return True


__all__ = ['update_or_create_item', 'delete_item']
