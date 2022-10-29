from flask import render_template, redirect, url_for

from webapp.db.issuance_of_cargo.changers import delete_issuance, save_issuance, delete_attachment, save_attachment
from webapp.db.issuance_of_cargo.fetchers import get_issuances, get_issuance_by_id, get_attachment_by_id
from webapp.db.storage.fetchers import get_storages
from webapp.db.order.fetchers import get_orders
from webapp.views.issuance_of_cargo.forms import IssuanceForm, AttachmentForm
from webapp.views.errors import (get_tempale_error_on_create_or_update,
                                 get_tempale_error_on_validation,
                                 get_tempale_error_on_mark_for_deleting)


def issuances_view():
    return render_template('issuance_list.html', issuances=get_issuances())


def issuance_view(issuance_id: int):
    issuance = get_issuance_by_id(id=issuance_id)
    form = IssuanceForm(obj=issuance)
    return render_template('issuance_item.html', form=form,
                           storages=get_storages(),
                           attachments=issuance.attachments)


def new_issuance_view():
    form = IssuanceForm()
    return render_template('issuance_item.html', form=form,
                           storages=get_storages(),
                           attachments=None)


def save_issuance_view():
    form = IssuanceForm()
    if form.validate_on_submit():
        if save_issuance(form):
            return redirect(url_for('issuances'))
        return get_tempale_error_on_create_or_update(form.errors)
    return get_tempale_error_on_validation(form.errors)


def delete_issuance_view(issuance_id: int):
    if delete_issuance(id=issuance_id):
        return redirect(url_for('issuances'))
    return get_tempale_error_on_mark_for_deleting()


def issuance_attachments_view(issuance_id: int):
    issuance = get_issuance_by_id(id=issuance_id)
    return render_template('issuance_attachment_list.html', attachments=issuance.attachments)


def issuance_attachment_view(attachment_id: int):
    attachment = get_attachment_by_id(id=attachment_id)
    form = AttachmentForm(obj=attachment)
    orders = get_orders()
    return render_template('issuance_attachment_item.html', form=form, orders=orders)


def issuance_new_attachment_view(issuance_id: int):
    form = AttachmentForm()
    form.issuance_id.data = issuance_id
    orders = get_orders()
    return render_template('issuance_attachment_item.html', form=form, orders=orders)


def issuance_save_attachment_view():
    form = AttachmentForm()
    if form.validate_on_submit():
        if save_attachment(form):
            return redirect(url_for('show_issuance', issuance_id=form.issuance_id.data))
        return render_template("crud_error.html", content='error on create or update storage info')
    return render_template("crud_error.html", content=f"error on validation {form.errors}")


def issuance_delete_attachment_view(attachment_id: int):
    attachment = get_attachment_by_id(id=attachment_id)
    issuance_id = attachment.issuance_id
    if delete_attachment(id=attachment_id):
        return redirect(url_for('show_issuance', issuance_id=issuance_id))
    return render_template("crud_error.html", content='error on mark attachment for deleting')
