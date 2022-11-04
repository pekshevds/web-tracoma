from webapp.urls.common_urls import add_common_urls
from webapp.urls.movement_urls import add_movement_urls
from webapp.urls.issuance_urls import add_issuance_urls


def add_urls(app):
    add_common_urls(app)
    add_movement_urls(app)
    add_issuance_urls(app)
