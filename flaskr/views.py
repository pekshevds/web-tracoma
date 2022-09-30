from xmlrpc.client import boolean
from flask import render_template, redirect, url_for
from flaskr.samples import get_storages, get_storage_by_id
from flaskr.changes import delete_storage_by_id, add_storage, update_storage


def get_home_view():
    return render_template('index.html')


def get_about_view():
    return render_template('about.html')


def get_storages_view(storage_type=1):
    return render_template('storage_list.html', storages=get_storages(storage_type=storage_type))


def get_new_storage_view():
    return render_template('storage_item.html', storages=None)


def get_storage_view(storage_id: int):
    return render_template('storage_item.html', storage=get_storage_by_id(storage_id))


def get_storeges_after_deleting_by_id(storage_id: int):
    delete_storage_by_id(storage_id)
    return redirect(url_for('storages'))


def get_storeges_after_create_update_by_id(storage_id: int, title: str, inn: str='', \
                                            is_internal: bool=False, is_employee: bool=False, \
                                            kpp: str='', weight: float=.0, volume: float=.0, \
                                            type: int=1):
    if storage_id:
        update_storage(id=storage_id, title=title, inn=inn, is_internal=is_internal, \
            is_employee=is_employee, kpp=kpp,weight=weight, volume=volume, \
                type=type)
    else:        
        add_storage(title=title, inn=inn, is_internal=is_internal, \
            is_employee=is_employee, kpp=kpp,weight=weight, volume=volume, \
                type=type)

    return redirect(url_for('storages'))
