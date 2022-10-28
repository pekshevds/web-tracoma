from flask import render_template, redirect, url_for

from webapp.db.cargo_movement.changers import delete_movement, save_movement, delete_attachment, save_attachment
from webapp.db.cargo_movement.fetchers import get_movements, get_movement_by_id, get_attachment_by_id
from webapp.db.storage.fetchers import get_storages
from webapp.db.order.fetchers import get_orders
from webapp.views.cargo_movement.forms import MovementForm, AttachmentForm
from webapp.views.errors import (get_tempale_error_on_create_or_update,
                                 get_tempale_error_on_validation,
                                 get_tempale_error_on_mark_for_deleting)


def movements_view():
    return render_template('movement_list.html', movements=get_movements())


def movement_view(movement_id: int):
    movement = get_movement_by_id(id=movement_id)
    form = MovementForm(obj=movement)
    return render_template('movement_item.html', form=form,
                           shippers=get_storages(),
                           consignees=get_storages(),
                           attachments=movement.attachments)


def new_movement_view():
    form = MovementForm()
    return render_template('movement_item.html', form=form,
                           shippers=get_storages(),
                           consignees=get_storages(),
                           attachments=None)


def save_movement_view():
    form = MovementForm()
    if form.validate_on_submit():
        if save_movement(form):
            return redirect(url_for('movements'))
        return get_tempale_error_on_create_or_update(form.errors)
    return get_tempale_error_on_validation(form.errors)


def delete_movement_view(movement_id: int):
    if delete_movement(id=movement_id):
        return redirect(url_for('movements'))
    return get_tempale_error_on_mark_for_deleting()


def movement_attachments_view(movement_id: int):
    movement = get_movement_by_id(id=movement_id)
    return render_template('movement_attachment_list.html', attachments=movement.attachments)


def movement_attachment_view(attachment_id: int):
    attachment = get_attachment_by_id(id=attachment_id)
    form = AttachmentForm(obj=attachment)
    orders = get_orders()
    return render_template('movement_attachment_item.html', form=form, orders=orders)


def movement_new_attachment_view(movement_id: int):
    form = AttachmentForm()
    form.movement_id.data = movement_id
    orders = get_orders()
    return render_template('movement_attachment_item.html', form=form, orders=orders)


def movement_save_attachment_view():
    form = AttachmentForm()
    if form.validate_on_submit():
        if save_attachment(form):
            return redirect(url_for('show_movement', movement_id=form.movement_id.data))
        return render_template("crud_error.html", content='error on create or update storage info')
    return render_template("crud_error.html", content=f"error on validation {form.errors}")


def movement_delete_attachment_view(attachment_id: int):
    attachment = get_attachment_by_id(id=attachment_id)
    movement_id = attachment.movement_id
    if delete_attachment(id=attachment_id):
        return redirect(url_for('show_movement', movement_id=movement_id))
    return render_template("crud_error.html", content='error on mark attachment for deleting')
