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
    except SQLAlchemyError:        
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
