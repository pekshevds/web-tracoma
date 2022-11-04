from flask.blueprints import Blueprint
from webapp.views.order import (OrderDetailView, OrderListView, OrderDeleteView,
                                AttachmentOrderDetailView, AttachmentOrderListView,
                                AttachmentOrderDeleteView)


def get_order_blueprints():
    blueprint = Blueprint(name='order', import_name='order', url_prefix='/orders')
    blueprint.add_url_rule('/', endpoint='orders', view_func=OrderListView.as_view('orders'))
    blueprint.add_url_rule('/show/<int:id>', endpoint='show_order', view_func=OrderDetailView.as_view('show_order'))
    blueprint.add_url_rule('/new', endpoint='new_order', view_func=OrderDetailView.as_view('new_order'))
    blueprint.add_url_rule('/delete/<int:id>', endpoint='delete_order',
                           view_func=OrderDeleteView.as_view('delete_order'))
    blueprint.add_url_rule('/save', endpoint='save_order', view_func=OrderDetailView.as_view('save_order'))

    blueprint.add_url_rule('/attachments/order/<int:order_id>', endpoint='attachments',
                           view_func=AttachmentOrderListView.as_view('attachments'))
    blueprint.add_url_rule('/attachments/show/<int:id>', endpoint='show_attachment',
                           view_func=AttachmentOrderDetailView.as_view('show_attachment'))
    blueprint.add_url_rule('/attachments/order/<int:order_id>/new', endpoint='new_attachment',
                           view_func=AttachmentOrderDetailView.as_view('new_attachment'))
    blueprint.add_url_rule('/attachments/delete/<int:id>', endpoint='delete_attachment',
                           view_func=AttachmentOrderDeleteView.as_view('delete_attachment'))
    blueprint.add_url_rule('/attachments/save', endpoint='save_attachment',
                           view_func=AttachmentOrderDetailView.as_view('save_attachment'))
    return blueprint
