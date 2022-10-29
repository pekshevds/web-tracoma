from webapp.views.storage import (storages_view, storages_by_kind_view,
                                  storage_view, new_storage_view, delete_storage_view, save_storage_view)


def add_storage_urls(app):
    prefix = "/storages"
    app.add_url_rule(f"{prefix}", endpoint="storages", view_func=storages_view)
    app.add_url_rule(f"{prefix}/kind/<int:storage_kind>", endpoint="storages_by_kind", view_func=storages_by_kind_view)
    app.add_url_rule(f"{prefix}/show/<int:storage_id>", endpoint="show_storage", view_func=storage_view)
    app.add_url_rule(f"{prefix}/new/<int:storage_kind>", endpoint="new_storage", view_func=new_storage_view)
    app.add_url_rule(f"{prefix}/delete/<int:storage_id>", endpoint="delete_storage", view_func=delete_storage_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_storage", view_func=save_storage_view, methods=['POST'])
