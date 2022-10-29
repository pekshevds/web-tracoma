from webapp.views.point import (delete_point_view, points_view, point_view,
                                new_point_view, save_point_view)


def add_point_urls(app):
    prefix = "/points"
    app.add_url_rule(f"{prefix}", endpoint="points", view_func=points_view)
    app.add_url_rule(f"{prefix}/show/<int:point_id>", endpoint="show_point", view_func=point_view)
    app.add_url_rule(f"{prefix}/new", endpoint="new_point", view_func=new_point_view)
    app.add_url_rule(f"{prefix}/delete/<int:point_id>", endpoint="delete_point", view_func=delete_point_view)
    app.add_url_rule(f"{prefix}/save", endpoint="save_point", view_func=save_point_view, methods=['POST'])
