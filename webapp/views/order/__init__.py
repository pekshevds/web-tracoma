import imp
from flask import render_template, redirect, url_for

from webapp.db.storage.fetchers import get_carriers, get_counteragents
from webapp.db.order.fetchers import get_orders, get_order_by_id
from webapp.db.order.changers import update_or_create_order, delete_order
from webapp.views.order.forms import OrderForm
from webapp.db.point.fetchers import get_points


def orders_view():
    return render_template('order_list.html', orders=get_orders())


def order_view(order_id: int):
    order = get_order_by_id(id=order_id)
    form = OrderForm()    
    form.id.data = order.id
    form.title.data = order.title
    form.carrier_id.data = order.carrier_id
    form.consignee_id.data = order.consignee_id
    form.consignee_address.data = order.consignee_address
    form.consignee_contact_id.data = order.consignee_contact_id
    form.consignee_phone.data = order.consignee_phone
    form.declared.data = order.declared
    form.desc.data = order.desc
    form.point_from_id.data = order.point_from_id
    form.point_to_id.data = order.point_to_id
    form.shipper_id.data = order.shipper_id
    form.shipper_address.data = order.shipper_address
    form.shipper_contact_id.data = order.shipper_contact_id
    form.shipper_phone.data = order.shipper_phone
    form.weight.data = order.weight
    form.volume.data = order.volume

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
    if form.validate_on_submit():
        if update_or_create_order(id=form.id.data, title=form.title.data, carrier_id=form.carrier_id.data,
        consignee_id=form.consignee_id.data, consignee_address=form.consignee_address.data, 
        consignee_contact_id=form.consignee_contact_id.data, consignee_phone=form.consignee_phone.data,
        declared=form.declared.data, desc=form.desc.data, point_from_id=form.point_from_id.data, 
        point_to_id=form.point_to_id.data, shipper_id=form.shipper_id.data, shipper_address=form.shipper_address.data,
        shipper_contact_id=form.shipper_contact_id.data, shipper_phone=form.shipper_phone.data, weight=form.weight.data, 
        volume=form.volume.data):
            return redirect(url_for('orders'))
        return render_template("crud_error.html", content='error on create or update order info')
    return render_template("crud_error.html", content='error on validation')


def delete_order_view(order_id: int):
    if delete_order(id=order_id):
        return redirect(url_for('orders'))
    return render_template("crud_error.html", content='error on mark order for deleting')
