from flask import render_template, redirect, url_for
from webapp.db.storage.fetchers import get_storages, get_storages_by_kind, get_storage_by_id
from webapp.db.storage.changers import delete_storage, save_storage
from webapp.views.storage.forms import StorageForm
from webapp.db.common import db
from webapp.db import Storage


def storages_view():
    return render_template('storage_list.html', storages=get_storages())


def storages_by_kind_view(storage_kind: int):
    return render_template('storage_list.html', storages=get_storages_by_kind(kind=storage_kind))


def storage_view(storage_id: int):
    storage = get_storage_by_id(id=storage_id)
    form = StorageForm(obj=storage)

    return render_template('storage_item.html', form=form)


def new_storage_view(storage_kind: int):
    form = StorageForm()
    form.kind.data = storage_kind
    return render_template('storage_item.html', form=form)


def save_storage_view():
    form = StorageForm()
    if form.validate_on_submit():
        if save_storage(form):
            return redirect(url_for('storages'))
        return render_template("crud_error.html", content='error on create or update storage info')
    return render_template("crud_error.html", content='error on validation')


def delete_storage_view(storage_id: int):
    if delete_storage(id=storage_id):
        return redirect(url_for('storages'))
    return render_template("crud_error.html", content='error on mark storage for deleting')
