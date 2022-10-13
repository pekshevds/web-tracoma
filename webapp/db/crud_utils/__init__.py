from sqlalchemy.exc import SQLAlchemyError


def update_or_create_item(id: int, db, get_func, object, **kwargs):
    item = get_func(id=id)
    if not item:
        item = object()

    for key, value in kwargs.items():        
        if hasattr(item, key):
            setattr(item, key, value)    
    
    db.session.add(item)
    try:        
        db.session.commit()
    except SQLAlchemyError:
        return False
    return True


def delete_item(id: int, db, get_func):
    item = get_func(id=id)
    if item:
        item.is_deleted = True
        db.session.add(item)
        try:            
            db.session.commit()
        except SQLAlchemyError:
            return False
    return True