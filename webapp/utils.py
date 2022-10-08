
def prepare_point_values(values):
    id = values.get("id", 0)
    try:
        id = int(id)
    except (ValueError, TypeError):
        id = 0        
    title = values.get("title", "new item")
    short = values.get("short", "")
    return id, title, short


def prepare_storage_values(values):
    id = values.get("id", 0)
    try:
        id = int(id)
    except (ValueError, TypeError):
        id = 0        
    title = values.get("title", "new item")
    inn = values.get("inn", "")
    kpp = values.get("kpp", "")
    is_internal = values.get("is_internal", False)
    if isinstance(is_internal, str):
        if is_internal == "on":
            is_internal = True
        else:
            is_internal = False
    is_employee = values.get("is_employee", False)
    if isinstance(is_employee, str):
        if is_employee == "on":
            is_employee = True
        else:
            is_employee = False
    kind = values.get("kind", 0)
    try:
        kind = int(kind)
    except (ValueError, TypeError):
        kind = 0
    weight = values.get("weight", 0)
    try:
        weight = float(weight)
    except (ValueError, TypeError):
        weight = .0
    volume = values.get("volume", 0)
    try:
        volume = float(volume)
    except (ValueError, TypeError):
        volume = .0

    return id, title, inn, kpp, is_internal, is_employee, kind, weight, volume
