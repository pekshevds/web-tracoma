from flask import render_template, redirect, url_for

from webapp.db.order.fetchers import get_orders
from webapp.db.storage.fetchers import get_storages
from webapp.db.receipt_of_cargo.fetchers import get_receipts, get_attachments, get_attachment_by_id
from webapp.db.receipt_of_cargo.changers import delete_receipt, delete_attachment
from webapp.views.receipt_of_cargo.forms import ReceiptForm, AttachmentForm
from webapp.views.common import BaseView
from flask_views.base import TemplateView


class ReceiptDetailView(BaseView):
    form_class = ReceiptForm
    template_name = 'receipt_item.html'
    self_url_name = 'receipt.show_receipt'

    def get(self, *args, **kwargs):
        receipt_id = kwargs.get("id", 0)
        object = super().get_object_by_id(id=receipt_id)
        if object:
            form = super().initial_form_values(object)
        else:
            form = self.get_form()
        return render_template(self.template_name, form=form,
                               storages=get_storages(),
                               attachments=get_attachments(receipt_id=receipt_id))


class ReceiptListView(TemplateView):
    template_name = 'receipt_list.html'

    def get(self, *args, **kwargs):
        return render_template(self.template_name, receipts=get_receipts())


class ReceiptDeleteView(TemplateView):
    success_url_name = 'receipt.receipts'

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        if delete_receipt(id=id):
            return redirect(url_for(self.success_url_name))
        return render_template("crud_error.html", content='error on mark point for deleting')


class AttachmentReceiptDetailView(BaseView):
    form_class = AttachmentForm
    template_name = 'receipt_attachment_item.html'
    self_url_name = 'receipt.show_attachment'

    def get(self, *args, **kwargs):
        object = self.get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = self.initial_form_values(object)
        else:
            form = self.get_form()
            form.receipt_id.data = kwargs.get("receipt_id", 0)
        return render_template(self.template_name, form=form, orders=get_orders())


class AttachmentReceiptListView(TemplateView):
    template_name = 'receipt_attachment_list.html'

    def get(self, *args, **kwargs):
        receipt_id = kwargs.get("receipt_id", 0)
        return render_template(self.template_name, attachments=get_attachments(receipt_id=receipt_id))


class AttachmentReceiptDeleteView(TemplateView):

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        attachment = get_attachment_by_id(id=id)
        receipt_id = attachment.receipt_id
        if delete_attachment(id=id):
            return redirect(url_for('receipt.show_receipt', id=receipt_id))
        return render_template("crud_error.html", content='error on mark point for deleting')
