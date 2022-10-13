from flask import render_template, request, redirect, url_for
from webapp.db.storage.fetchers import get_storages, get_storages_by_kind, get_storage_by_id
from webapp.db.storage.changers import update_or_create_storage, delete_storage

from webapp.utils import prepare_storage_values


def storages_view():
    return render_template('storage_list.html', storages=get_storages())


def storages_by_kind_view(storage_kind: int):
    return render_template('storage_list.html', storages=get_storages_by_kind(kind=storage_kind))


def storage_view(storage_id: int):
    return render_template('storage_item.html', storage=get_storage_by_id(id=storage_id))


def new_storage_view(storage_kind: int):
    return render_template('storage_item.html', storage=None, storage_kind=storage_kind)


def save_storage_view():    
    id, title, inn, kpp, is_internal, is_employee, kind, weight, volume = prepare_storage_values(request.values)
    if update_or_create_storage(id=id, title=title, kind=kind, inn=inn, kpp=kpp, is_internal=is_internal,\
        is_employee=is_employee, weight=weight, volume=volume):
        return redirect(url_for('storages'))
    return render_template("crud_error.html", content='error on create or update storage info')


def delete_storage_view(storage_id: int):    
    if delete_storage(id=storage_id):
        return redirect(url_for('storages'))
    return render_template("crud_error.html", content='error on mark storage for deleting')
