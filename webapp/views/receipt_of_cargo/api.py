from flask import render_template, redirect, url_for

from webapp.db.receipt_of_cargo.changers import delete_receipt, save_receipt, delete_attachment, save_attachment
from webapp.db.receipt_of_cargo.fetchers import get_receipts, get_receipt_by_id, get_attachment_by_id
from webapp.db.storage.fetchers import get_storages
from webapp.db.order.fetchers import get_orders
from webapp.views.receipt_of_cargo.forms import ReceiptForm, AttachmentForm
from webapp.views.errors import (get_tempale_error_on_create_or_update,
                                 get_tempale_error_on_validation,
                                 get_tempale_error_on_mark_for_deleting)


def receipts_view():
    return render_template('receipt_list.html', receipts=get_receipts())


def receipt_view(receipt_id: int):
    reciept = get_receipt_by_id(id=receipt_id)
    form = ReceiptForm(obj=reciept)
    return render_template('receipt_item.html', form=form,
                           storages=get_storages(),
                           attachments=reciept.attachments)


def new_receipt_view():
    form = ReceiptForm()
    return render_template('receipt_item.html', form=form,
                           storages=get_storages(),
                           attachments=None)


def save_receipt_view():
    form = ReceiptForm()
    if form.validate_on_submit():
        if save_receipt(form):
            return redirect(url_for('receipts'))
        return get_tempale_error_on_create_or_update(form.errors)
    return get_tempale_error_on_validation(form.errors)


def delete_receipt_view(receipt_id: int):
    if delete_receipt(id=receipt_id):
        return redirect(url_for('receipts'))
    return get_tempale_error_on_mark_for_deleting()


def receipt_attachments_view(receipt_id: int):
    receipt = get_receipt_by_id(id=receipt_id)
    return render_template('receipt_attachment_list.html', attachments=receipt.attachments)


def receipt_attachment_view(attachment_id: int):
    attachment = get_attachment_by_id(id=attachment_id)
    form = AttachmentForm(obj=attachment)
    orders = get_orders()
    return render_template('receipt_attachment_item.html', form=form, orders=orders)


def receipt_new_attachment_view(receipt_id: int):
    form = AttachmentForm()
    form.receipt_id.data = receipt_id
    orders = get_orders()
    return render_template('receipt_attachment_item.html', form=form, orders=orders)


def receipt_save_attachment_view():
    form = AttachmentForm()
    if form.validate_on_submit():
        if save_attachment(form):
            return redirect(url_for('show_receipt', receipt_id=form.receipt_id.data))
        return render_template("crud_error.html", content='error on create or update storage info')
    return render_template("crud_error.html", content=f"error on validation {form.errors}")


def receipt_delete_attachment_view(attachment_id: int):
    attachment = get_attachment_by_id(id=attachment_id)
    receipt_id = attachment.receipt_id
    if delete_attachment(id=attachment_id):
        return redirect(url_for('show_receipt', receipt_id=receipt_id))
    return render_template("crud_error.html", content='error on mark attachment for deleting')
