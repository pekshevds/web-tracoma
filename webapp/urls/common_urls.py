from webapp.views import home_view, about_view


def add_common_urls(app):
    app.add_url_rule("/", endpoint="home", view_func=home_view)
    app.add_url_rule("/home", endpoint="home", view_func=home_view)
    app.add_url_rule("/about", endpoint="about", view_func=about_view)
