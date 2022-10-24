from webapp.db import Storage


def get_storages():
    return Storage.query.filter().all()


def get_storages_by_kind(kind: int):
    return Storage.query.filter(Storage.kind == kind).all()


def get_persons():
    return get_storages_by_kind(kind=1)


def get_companies():
    return get_storages_by_kind(kind=2)


def get_storage_by_id(id: int):
    return Storage.query.get(id)


def get_carriers():
    """gets a list of carriers (own legal entities)
    """
    return Storage.query.filter(Storage.is_internal == (True)).all()


def get_counteragents():
    """gets a list of counteragents (shippers and consignee)
    """
    return Storage.query.filter(
        Storage.is_internal == (True)).all()


def get_employees():
    """gets a list of employees
    """
    return Storage.query.filter(Storage.is_internal == (False), Storage.is_employee == (True), Storage.kind == 1).all()
