from webapp.views.order import (delete_order_view, orders_view, order_view,
                                new_order_view, save_order_view,
                                order_attachments_view, order_attachment_view,
                                order_new_attachment_view, order_save_attachment_view, order_delete_attachment_view)


def add_order_urls(app):
    prefix = "/orders"
    app.add_url_rule(f"{prefix}", endpoint="orders", view_func=orders_view)
    app.add_url_rule(f"{prefix}/show/<int:order_id>", endpoint="show_order", view_func=order_view)
    app.add_url_rule(f"{prefix}/new", endpoint="new_order", view_func=new_order_view)
    app.add_url_rule(f"{prefix}/delete/<int:order_id>", endpoint="delete_order", view_func=delete_order_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_order", view_func=save_order_view, methods=['POST'])
    app.add_url_rule(f"{prefix}/attachments/order/<int:order_id>", endpoint="order_attachments",
                     view_func=order_attachments_view)
    app.add_url_rule(f"{prefix}/attachments/show/<int:attachment_id>", endpoint="show_order_attachment",
                     view_func=order_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/new/order/<int:order_id>", endpoint="new_order_attachment",
                     view_func=order_new_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/delete/<int:attachment_id>", endpoint="delete_order_attachment",
                     view_func=order_delete_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/save", endpoint="save_order_attachment", methods=['POST'],
                     view_func=order_save_attachment_view)
