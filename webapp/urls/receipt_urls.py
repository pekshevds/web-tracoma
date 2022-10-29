from webapp.views.receipt_of_cargo import (delete_receipt_view, receipts_view, receipt_view,
                                           new_receipt_view, save_receipt_view,
                                           receipt_attachments_view, receipt_attachment_view,
                                           receipt_new_attachment_view, receipt_save_attachment_view,
                                           receipt_delete_attachment_view)


def add_receipt_urls(app):
    prefix = "/receipts"
    app.add_url_rule(f"{prefix}", endpoint="receipts", view_func=receipts_view)
    app.add_url_rule(f"{prefix}/show/<int:receipt_id>", endpoint="show_receipt", view_func=receipt_view)
    app.add_url_rule(f"{prefix}/new", endpoint="new_receipt", view_func=new_receipt_view)
    app.add_url_rule(f"{prefix}/delete/<int:receipt_id>", endpoint="delete_receipt", view_func=delete_receipt_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_receipt", view_func=save_receipt_view, methods=['POST'])
    app.add_url_rule(f"{prefix}/attachments/receipt/<int:receipt_id>", endpoint="receipt_attachments",
                     view_func=receipt_attachments_view)
    app.add_url_rule(f"{prefix}/attachments/show/<int:attachment_id>", endpoint="show_receipt_attachment",
                     view_func=receipt_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/new/receipt/<int:receipt_id>", endpoint="new_receipt_attachment",
                     view_func=receipt_new_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/delete/<int:attachment_id>", endpoint="delete_receipt_attachment",
                     view_func=receipt_delete_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/save", endpoint="save_receipt_attachment", methods=['POST'],
                     view_func=receipt_save_attachment_view)
