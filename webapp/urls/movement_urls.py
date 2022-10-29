from webapp.views.cargo_movement import (delete_movement_view, movements_view, movement_view,
                                         new_movement_view, save_movement_view,
                                         movement_attachments_view, movement_attachment_view,
                                         movement_new_attachment_view, movement_save_attachment_view,
                                         movement_delete_attachment_view)


def add_movement_urls(app):
    prefix = "/movements"
    app.add_url_rule(f"{prefix}", endpoint="movements", view_func=movements_view)
    app.add_url_rule(f"{prefix}/show/<int:movement_id>", endpoint="show_movement", view_func=movement_view)
    app.add_url_rule(f"{prefix}/new", endpoint="new_movement", view_func=new_movement_view)
    app.add_url_rule(f"{prefix}/delete/<int:movement_id>", endpoint="delete_movement", view_func=delete_movement_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_movement", view_func=save_movement_view, methods=['POST'])
    app.add_url_rule(f"{prefix}/attachments/movement/<int:movement_id>", endpoint="movement_attachments",
                     view_func=movement_attachments_view)
    app.add_url_rule(f"{prefix}/attachments/show/<int:attachment_id>", endpoint="show_movement_attachment",
                     view_func=movement_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/new/movement/<int:movement_id>", endpoint="new_movement_attachment",
                     view_func=movement_new_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/delete/<int:attachment_id>", endpoint="delete_movement_attachment",
                     view_func=movement_delete_attachment_view)
    app.add_url_rule(f"{prefix}/attachments/save", endpoint="save_movement_attachment", methods=['POST'],
                     view_func=movement_save_attachment_view)
