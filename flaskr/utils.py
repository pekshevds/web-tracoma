def validate_paramas_for_storage(**kwargs):
    id = kwargs.get('id')
    if id:
        try:
            id = int(id)
        except ValueError:
            id = 0
    else:
        id = 0
    
    title = kwargs.get('title').strip() 
    inn = kwargs.get('inn').strip()
    
    is_internal = kwargs.get('is_internal')
    if is_internal:
        if is_internal == 'on':
            is_internal = True
        else:
            is_internal = False
    else:
        is_internal = False

    is_employee = kwargs.get('is_employee')
    if is_employee:
        if is_employee == 'on':
            is_employee = True
        else:
            is_employee = False
    else:
        is_employee = False
   
    kpp = kwargs.get('kpp').strip()
   
    weight = kwargs.get('weight')
    if weight:
        try:
            weight = float(weight)
        except ValueError:
            weight = .0
    else:
        weight = .0
    volume = kwargs.get('volume')
    
    if volume:
        try:
            volume = float(volume)
        except ValueError:
            volume = .0
    else:
        volume = .0
    
    kind = kwargs.get('kind')    
    if kind:
        try:
            kind = int(kind)
        except ValueError:
            kind = 1
    else:
        kind = 1

    return id, title, inn, is_internal, is_employee, kpp, weight, volume, kind