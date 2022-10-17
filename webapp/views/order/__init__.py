import imp
from flask import render_template, redirect, url_for

from webapp.db.storage.fetchers import get_carriers, get_counteragents
from webapp.db.order.fetchers import get_orders, get_order_by_id
from webapp.db.order.changers import update_or_create_order, delete_order
from webapp.views.order.forms import OrderForm
from webapp.db.point.fetchers import get_points


def orders_view():
    return render_template('order_list.html', points=get_orders())


def order_view(point_id: int):
    order = get_order_by_id(id=point_id)
    form = OrderForm()
    form.id.data = order.id
    form.title.data = order.title    

    return render_template('order_item.html', form=form, 
        carriers=get_carriers(), 
        counteragents=get_counteragents(),
        points=get_points())


def new_order_view():
    form = OrderForm()    
    return render_template('order_item.html', form=form, 
        carriers=get_carriers(), 
        counteragents=get_counteragents(),
        points=get_points())


def save_order_view():
    form = OrderForm()
    print(form.data)
    if form.validate_on_submit():
        if update_or_create_order(id=form.id.data, title=form.title.data):
            return redirect(url_for('orders'))
        return render_template("crud_error.html", content='error on create or update order info')
    return render_template("crud_error.html", content='error on validation')


def delete_order_view(order_id: int):
    if delete_order(id=order_id):
        return redirect(url_for('orders'))
    return render_template("crud_error.html", content='error on mark order for deleting')
