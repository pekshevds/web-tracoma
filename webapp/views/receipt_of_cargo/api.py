from flask import render_template, redirect, url_for

from webapp.db.order.fetchers import get_orders
from webapp.db.receipt_of_cargo.models import ReceiptOfCargo, AttachmentReceiptOfCargo
from webapp.db.receipt_of_cargo.fetchers import get_receipts, get_attachments, get_attachment_by_id
from webapp.db.receipt_of_cargo.changers import delete_receipt, delete_attachment
from webapp.views.receipt_of_cargo.forms import ReceiptForm, AttachmentForm
from webapp.views.common import DetailView, ListView, DeleteView


class ReceiptDetailView(DetailView):
    form_class = ReceiptForm
    template_name = 'receipt_item.html'
    self_url_name = 'receipt.show_receipt'
    model = ReceiptOfCargo

    def get_attachments(self, id: int):
        return get_attachments(id)

class ReceiptListView(ListView):
    template_name = 'receipt_list.html'

    def get_context_data(self, **kwargs):
        kwargs['receipts'] = get_receipts()
        return kwargs


class ReceiptDeleteView(DeleteView):
    success_url_name = 'receipt.receipts'

    def delete(self, id: int):
        return delete_receipt(id)


class AttachmentReceiptDetailView(DetailView):
    form_class = AttachmentForm
    template_name = 'receipt_attachment_item.html'
    self_url_name = 'receipt.show_attachment'
    model = AttachmentReceiptOfCargo

    def get(self, *args, **kwargs):
        object = self.get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = self.initial_form_values(object)
        else:
            form = self.get_form()
            form.receipt_id.data = kwargs.get("receipt_id", 0)
        return render_template(self.template_name, form=form, orders=get_orders())


class AttachmentReceiptListView(ListView):
    template_name = 'receipt_attachment_list.html'

    def get_context_data(self, **kwargs):
        receipt_id = kwargs.get("receipt_id", 0)
        kwargs['attachments'] = get_attachments(receipt_id=receipt_id)
        return kwargs


class AttachmentReceiptDeleteView(DeleteView):
    success_url_name = 'receipt.show_receipt'

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        attachment = get_attachment_by_id(id=id)
        receipt_id = attachment.receipt_id
        if delete_attachment(id=id):
            return redirect(url_for(self.success_url_name, id=receipt_id))
        return render_template("crud_error.html", content='error on mark point for deleting')
