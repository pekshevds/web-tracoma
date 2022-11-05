from flask import render_template, redirect, url_for

from webapp.db.order.fetchers import get_orders
from webapp.db.issuance_of_cargo.models import IssuanceOfCargo, AttachmentIssuanceOfCargo
from webapp.db.issuance_of_cargo.fetchers import get_issuances, get_attachments, get_attachment_by_id
from webapp.db.issuance_of_cargo.changers import delete_issuance, delete_attachment
from webapp.views.issuance_of_cargo.forms import IssuanceForm, AttachmentForm
from webapp.views.common import DetailView, ListView, DeleteView


class IssuanceDetailView(DetailView):
    form_class = IssuanceForm
    template_name = 'issuance_item.html'
    self_url_name = 'issuance.show_issuance'
    model = IssuanceOfCargo

    def get_attachments(self, id: int):
        return get_attachments(id)


class IssuanceListView(ListView):
    template_name = 'issuance_list.html'

    def get_context_data(self, **kwargs):
        kwargs['issuances'] = get_issuances()
        return kwargs


class IssuanceDeleteView(DeleteView):
    success_url_name = 'issuance.issuances'

    def delete(self, id: int):
        return delete_issuance(id)


class AttachmentIssuanceDetailView(DetailView):
    form_class = AttachmentForm
    template_name = 'issuance_attachment_item.html'
    self_url_name = 'issuance.show_attachment'
    model = AttachmentIssuanceOfCargo

    def get(self, *args, **kwargs):
        object = self.get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = self.initial_form_values(object)
        else:
            form = self.get_form()
            form.issuance_id.data = kwargs.get("issuance_id", 0)
        return render_template(self.template_name, form=form, orders=get_orders())


class AttachmentIssuanceListView(ListView):
    template_name = 'issuance_attachment_list.html'

    def get_context_data(self, **kwargs):
        issuance_id = kwargs.get("issuance_id", 0)
        kwargs['attachments'] = get_attachments(issuance_id=issuance_id)
        return kwargs


class AttachmentIssuanceDeleteView(DeleteView):

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        attachment = get_attachment_by_id(id=id)
        issuance_id = attachment.issuance_id
        if delete_attachment(id=id):
            return redirect(url_for('issuance.show_issuance', id=issuance_id))
        return render_template("crud_error.html", content='error on mark point for deleting')
