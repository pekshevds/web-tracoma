from flask import render_template, redirect, url_for

from webapp.db.order.fetchers import get_orders
from webapp.db.cargo_movement.models import CargoMovement, AttachmentCargoMovement
from webapp.db.cargo_movement.fetchers import get_movements, get_attachments, get_attachment_by_id
from webapp.db.cargo_movement.changers import delete_movement, delete_attachment
from webapp.views.cargo_movement.forms import MovementForm, AttachmentForm
from webapp.views.common import DetailView, ListView, DeleteView


class MovementDetailView(DetailView):
    form_class = MovementForm
    template_name = 'movement_item.html'
    self_url_name = 'movement.show_movement'
    model = CargoMovement

    def get_attachments(self, id: int):
        return get_attachments(id)


class MovementListView(ListView):
    template_name = 'movement_list.html'

    def get_context_data(self, **kwargs):
        kwargs['movements'] = get_movements()
        return kwargs


class MovementDeleteView(DeleteView):
    success_url_name = 'movement.movements'

    def delete(self, id: int):
        return delete_movement(id)

class AttachmentMovementDetailView(DetailView):
    form_class = AttachmentForm
    template_name = 'movement_attachment_item.html'
    self_url_name = 'movement.show_attachment'
    model = AttachmentCargoMovement

    def get(self, *args, **kwargs):
        object = self.get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = self.initial_form_values(object)
        else:
            form = self.get_form()
            form.movement_id.data = kwargs.get("movement_id", 0)
        return render_template(self.template_name, form=form, orders=get_orders())


class AttachmentMovementListView(ListView):
    template_name = 'movement_attachment_list.html'

    def get_context_data(self, **kwargs):
        movement_id = kwargs.get("movement_id", 0)
        kwargs['attachments'] = get_attachments(movement_id=movement_id)
        return kwargs


class AttachmentMovementDeleteView(DeleteView):

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        attachment = get_attachment_by_id(id=id)
        movement_id = attachment.movement_id
        if delete_attachment(id=id):
            return redirect(url_for('movement.show_movement', id=movement_id))
        return render_template("crud_error.html", content='error on mark point for deleting')
