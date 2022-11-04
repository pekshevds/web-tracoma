from flask import render_template, redirect, url_for

from webapp.db.order.fetchers import get_orders
from webapp.db.storage.fetchers import get_storages
from webapp.db.cargo_movement.fetchers import get_movements, get_attachments, get_attachment_by_id
from webapp.db.cargo_movement.changers import delete_movement, delete_attachment
from webapp.views.cargo_movement.forms import MovementForm, AttachmentForm
from webapp.views.common import BaseView
from flask_views.base import TemplateView


class MovementDetailView(BaseView):
    form_class = MovementForm
    template_name = 'movement_item.html'
    self_url_name = 'movement.show_movement'

    def get(self, *args, **kwargs):
        movement_id = kwargs.get("id", 0)
        object = super().get_object_by_id(id=movement_id)
        if object:
            form = super().initial_form_values(object)
        else:
            form = self.get_form()
        return render_template(self.template_name, form=form,
                               shippers=get_storages(),
                               consignees=get_storages(),
                               attachments=get_attachments(movement_id=movement_id))


class MovementListView(TemplateView):
    template_name = 'movement_list.html'

    def get(self, *args, **kwargs):
        return render_template(self.template_name, movements=get_movements())


class MovementDeleteView(TemplateView):
    success_url_name = 'movement.movements'

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        if delete_movement(id=id):
            return redirect(url_for(self.success_url_name))
        return render_template("crud_error.html", content='error on mark point for deleting')


class AttachmentMovementDetailView(BaseView):
    form_class = AttachmentForm
    template_name = 'movement_attachment_item.html'
    self_url_name = 'movement.show_attachment'

    def get(self, *args, **kwargs):
        object = self.get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = self.initial_form_values(object)
        else:
            form = self.get_form()
            form.movement_id.data = kwargs.get("movement_id", 0)
        return render_template(self.template_name, form=form, orders=get_orders())


class AttachmentMovementListView(TemplateView):
    template_name = 'movement_attachment_list.html'

    def get(self, *args, **kwargs):
        movement_id = kwargs.get("movement_id", 0)
        return render_template(self.template_name, attachments=get_attachments(movement_id=movement_id))


class AttachmentMovementDeleteView(TemplateView):

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        attachment = get_attachment_by_id(id=id)
        movement_id = attachment.movement_id
        if delete_attachment(id=id):
            return redirect(url_for('movement.show_movement', id=movement_id))
        return render_template("crud_error.html", content='error on mark point for deleting')
