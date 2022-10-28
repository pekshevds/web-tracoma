from flask import render_template, redirect, url_for

from webapp.db.attachment.fetchers import get_attachments
from webapp.db.order.changers import delete_order, save_order
from webapp.db.order.fetchers import get_orders, get_order_by_id
from webapp.db.point.fetchers import get_points
from webapp.db.storage.fetchers import get_carriers, get_counteragents
from webapp.views.order.forms import OrderForm
from webapp.views.errors import (get_tempale_error_on_create_or_update,
                                 get_tempale_error_on_validation,
                                 get_tempale_error_on_mark_order_for_deleting)


def orders_view():
    return render_template('order_list.html', orders=get_orders())


def order_view(order_id: int):
    order = get_order_by_id(id=order_id)
    form = OrderForm(obj=order)
    return render_template('order_item.html', form=form,
                           carriers=get_carriers(),
                           counteragents=get_counteragents(),
                           points=get_points(),
                           attachments=get_attachments(order_id=order_id))


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
    return get_tempale_error_on_mark_order_for_deleting()
