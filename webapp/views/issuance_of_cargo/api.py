from flask import render_template, redirect, url_for

from webapp.db.order.fetchers import get_orders
from webapp.db.storage.fetchers import get_storages
from webapp.db.issuance_of_cargo.fetchers import get_issuances, get_attachments, get_attachment_by_id
from webapp.db.issuance_of_cargo.changers import delete_issuance, delete_attachment
from webapp.views.issuance_of_cargo.forms import IssuanceForm, AttachmentForm
from webapp.views.common import BaseView
from flask_views.base import TemplateView


class IssuanceDetailView(BaseView):
    form_class = IssuanceForm
    template_name = 'issuance_item.html'
    self_url_name = 'issuance.show_issuance'

    def get(self, *args, **kwargs):
        issuance_id = kwargs.get("id", 0)
        object = super().get_object_by_id(id=issuance_id)
        if object:
            form = super().initial_form_values(object)
        else:
            form = self.get_form()
        return render_template(self.template_name, form=form,
                               storages=get_storages(),
                               attachments=get_attachments(issuance_id=issuance_id))


class IssuanceListView(TemplateView):
    template_name = 'issuance_list.html'

    def get(self, *args, **kwargs):
        return render_template(self.template_name, issuances=get_issuances())


class IssuanceDeleteView(TemplateView):
    success_url_name = 'issuance.issuances'

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        if delete_issuance(id=id):
            return redirect(url_for(self.success_url_name))
        return render_template("crud_error.html", content='error on mark point for deleting')


class AttachmentIssuanceDetailView(BaseView):
    form_class = AttachmentForm
    template_name = 'issuance_attachment_item.html'
    self_url_name = 'issuance.show_attachment'

    def get(self, *args, **kwargs):
        object = self.get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = self.initial_form_values(object)
        else:
            form = self.get_form()
            form.issuance_id.data = kwargs.get("issuance_id", 0)
        return render_template(self.template_name, form=form, orders=get_orders())


class AttachmentIssuanceListView(TemplateView):
    template_name = 'issuance_attachment_list.html'

    def get(self, *args, **kwargs):
        issuance_id = kwargs.get("issuance_id", 0)
        return render_template(self.template_name, attachments=get_attachments(issuance_id=issuance_id))


class AttachmentIssuanceDeleteView(TemplateView):

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        attachment = get_attachment_by_id(id=id)
        issuance_id = attachment.issuance_id
        if delete_attachment(id=id):
            return redirect(url_for('issuance.show_issuance', id=issuance_id))
        return render_template("crud_error.html", content='error on mark point for deleting')
