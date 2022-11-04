from flask.blueprints import Blueprint
from webapp.views.receipt_of_cargo import (ReceiptDetailView, ReceiptListView, ReceiptDeleteView,
                                           AttachmentReceiptDetailView, AttachmentReceiptListView,
                                           AttachmentReceiptDeleteView)


def get_receipt_blueprints():
    blueprint = Blueprint(name='receipt', import_name='receipt', url_prefix='/receipts')
    blueprint.add_url_rule('/', endpoint='receipts', view_func=ReceiptListView.as_view('receipts'))
    blueprint.add_url_rule('/show/<int:id>', endpoint='show_receipt',
                           view_func=ReceiptDetailView.as_view('show_receipt'))
    blueprint.add_url_rule('/new', endpoint='new_receipt', view_func=ReceiptDetailView.as_view('new_receipt'))
    blueprint.add_url_rule('/delete/<int:id>', endpoint='delete_receipt',
                           view_func=ReceiptDeleteView.as_view('delete_receipt'))
    blueprint.add_url_rule('/save', endpoint='save_receipt', view_func=ReceiptDetailView.as_view('save_receipt'))

    blueprint.add_url_rule('/attachments/receipt/<int:receipt_id>', endpoint='attachments',
                           view_func=AttachmentReceiptListView.as_view('attachments'))
    blueprint.add_url_rule('/attachments/show/<int:id>', endpoint='show_attachment',
                           view_func=AttachmentReceiptDetailView.as_view('show_attachment'))
    blueprint.add_url_rule('/attachments/order/<int:receipt_id>/new', endpoint='new_attachment',
                           view_func=AttachmentReceiptDetailView.as_view('new_attachment'))
    blueprint.add_url_rule('/attachments/delete/<int:id>', endpoint='delete_attachment',
                           view_func=AttachmentReceiptDeleteView.as_view('delete_attachment'))
    blueprint.add_url_rule('/attachments/save', endpoint='save_attachment',
                           view_func=AttachmentReceiptDetailView.as_view('save_attachment'))
    return blueprint
