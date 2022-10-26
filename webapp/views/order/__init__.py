from flask import render_template, redirect, url_for

from webapp.db.order.changers import delete_order, save_order, delete_attachment, save_attachment
from webapp.db.order.fetchers import get_orders, get_order_by_id, get_attachment_by_id
from webapp.db.point.fetchers import get_points
from webapp.db.storage.fetchers import get_carriers, get_counteragents
from webapp.views.order.forms import OrderForm, AttachmentForm
from webapp.views.errors import (get_tempale_error_on_create_or_update,
                                 get_tempale_error_on_validation,
                                 get_tempale_error_on_mark_for_deleting)


def orders_view():
    return render_template('order_list.html', orders=get_orders())


def order_view(order_id: int):
    order = get_order_by_id(id=order_id)
    form = OrderForm(obj=order)
    return render_template('order_item.html', form=form,
                           carriers=get_carriers(),
                           counteragents=get_counteragents(),
                           points=get_points(),
                           attachments=order.attachments)


def new_order_view():
    form = OrderForm()
    return render_template('order_item.html', form=form,
                           carriers=get_carriers(),
                           counteragents=get_counteragents(),
                           points=get_points(),
                           attachments=None)


def save_order_view():
    form = OrderForm()
    if form.validate_on_submit():
        if save_order(form):
            return redirect(url_for('orders'))
        return get_tempale_error_on_create_or_update(form.errors)
    return get_tempale_error_on_validation(form.errors)


def delete_order_view(order_id: int):
    if delete_order(id=order_id):
        return redirect(url_for('orders'))
    return get_tempale_error_on_mark_for_deleting()


def order_attachments_view(order_id: int):
    order = get_order_by_id(id=order_id)
    return render_template('order_attachment_list.html', attachments=order.attachments)


def order_attachment_view(attachment_id: int):
    attachment = get_attachment_by_id(id=attachment_id)
    form = AttachmentForm(obj=attachment)

    return render_template('order_attachment_item.html', form=form)


def order_new_attachment_view(order_id: int):
    form = AttachmentForm()
    form.order_id.data = order_id
    return render_template('order_attachment_item.html', form=form)


def order_save_attachment_view():
    form = AttachmentForm()
    if form.validate_on_submit():
        if save_attachment(form):
            return redirect(url_for('show_order', order_id=form.order_id.data))
        return render_template("crud_error.html", content='error on create or update storage info')
    return render_template("crud_error.html", content=f"error on validation {form.errors}")


def order_delete_attachment_view(attachment_id: int):
    if delete_attachment(id=attachment_id):
        attachment = get_attachment_by_id(id=attachment_id)
        return redirect(url_for('show_order', order_id=attachment.id))
    return render_template("crud_error.html", content='error on mark attachment for deleting')
