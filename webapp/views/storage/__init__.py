from flask import render_template, redirect, url_for
from webapp.db.storage.fetchers import get_storages, get_storages_by_kind, get_storage_by_id
from webapp.db.storage.changers import update_or_create_storage, delete_storage

from webapp.views.storage.forms import StorageForm


def storages_view():
    return render_template('storage_list.html', storages=get_storages())


def storages_by_kind_view(storage_kind: int):
    return render_template('storage_list.html', storages=get_storages_by_kind(kind=storage_kind))


def storage_view(storage_id: int):
    storage = get_storage_by_id(id=storage_id)
    form = StorageForm()
    form.id.data = storage.id
    form.title.data = storage.title
    form.is_internal.data = storage.is_internal
    form.is_employee.data = storage.is_employee
    form.kind.data = storage.kind
    form.inn.data = storage.inn
    form.kpp.data = storage.kpp
    form.weight.data = storage.weight
    form.volume.data = storage.volume
    return render_template('storage_item.html', form=form)


def new_storage_view(storage_kind: int):
    form = StorageForm()
    form.kind.data = storage_kind
    return render_template('storage_item.html', form=form)


def save_storage_view():
    form = StorageForm()
    if form.validate_on_submit():
        if update_or_create_storage(id=form.id.data, title=form.title.data, 
                                    is_internal=form.is_internal.data, is_employee=form.is_employee.data,
                                    kind=form.kind.data, inn=form.inn.data, kpp=form.kpp.data,
                                    weight=form.weight.data, volume=form.volume.data):
            return redirect(url_for('storages'))
        return render_template("crud_error.html", content='error on create or update storage info')
    return render_template("crud_error.html", content='error on validation')


def delete_storage_view(storage_id: int):    
    if delete_storage(id=storage_id):
        return redirect(url_for('storages'))
    return render_template("crud_error.html", content='error on mark storage for deleting')
