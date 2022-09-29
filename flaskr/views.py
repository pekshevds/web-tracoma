from flask import render_template, redirect, url_for
from flaskr.samples import get_storages, get_storage_by_id
from flaskr.changes import delete_storage_by_id, add_storage, update_storage


def get_home_view():
    return render_template('index.html')


def get_about_view():
    return render_template('about.html')


def get_storages_view():
    return render_template('storage_list.html', storages=get_storages())


def get_new_storage_view():
    return render_template('storage_item.html', storages=None)


def get_storage_view(storage_id: int):
    return render_template('storage_item.html', storage=get_storage_by_id(storage_id))


def get_storeges_after_deleting_by_id(storage_id: int):
    delete_storage_by_id(storage_id)
    return redirect(url_for('storages'))


def get_storeges_after_create_update_by_id(storage_id: int, title: str, inn: str):
    if storage_id == '':
        add_storage(title=title, inn=inn)
    else:
        update_storage(int(id), title=title, inn=inn)

    return redirect(url_for('storages'))
