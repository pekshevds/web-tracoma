from webapp.views.issuance_of_cargo import (delete_issuance_view, issuances_view, issuance_view,
                                            new_issuance_view, save_issuance_view,
                                            issuance_attachments_view, issuance_attachment_view,
                                            issuance_new_attachment_view, issuance_save_attachment_view,
                                            issuance_delete_attachment_view)


def add_issuance_urls(app):
    prefix = "/issuances"
    app.add_url_rule(f"{prefix}", endpoint="issuances", view_func=issuances_view)
    app.add_url_rule(f"{prefix}/show/<int:issuance_id>", endpoint="show_issuance", view_func=issuance_view)
    app.add_url_rule(f"{prefix}/new", endpoint="new_issuance", view_func=new_issuance_view)
    app.add_url_rule(f"{prefix}/delete/<int:issuance_id>", endpoint="delete_issuance", view_func=delete_issuance_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_issuance", view_func=save_issuance_view, methods=['POST'])
    app.add_url_rule(f"{prefix}/attachments/issuance/<int:issuance_id>", endpoint="issuance_attachments",
                     view_func=issuance_attachments_view)
    app.add_url_rule(f"{prefix}/attachments/show/<int:attachment_id>", endpoint="show_issuance_attachment",
                     view_func=issuance_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/new/issuance/<int:issuance_id>", endpoint="new_issuance_attachment",
                     view_func=issuance_new_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/delete/<int:attachment_id>", endpoint="delete_issuance_attachment",
                     view_func=issuance_delete_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/save", endpoint="save_issuance_attachment", methods=['POST'],
                     view_func=issuance_save_attachment_view)
