from flask.blueprints import Blueprint
from webapp.views.cargo_movement import (MovementDetailView, MovementListView, MovementDeleteView,
                                         AttachmentMovementDetailView, AttachmentMovementListView,
                                         AttachmentMovementDeleteView)


def get_movement_blueprints():
    blueprint = Blueprint(name='movement', import_name='movement', url_prefix='/movements')
    blueprint.add_url_rule('/', endpoint='movements', view_func=MovementListView.as_view('movements'))
    blueprint.add_url_rule('/show/<int:id>', endpoint='show_movement',
                           view_func=MovementDetailView.as_view('show_movement'))
    blueprint.add_url_rule('/new', endpoint='new_movement', view_func=MovementDetailView.as_view('new_movement'))
    blueprint.add_url_rule('/delete/<int:id>', endpoint='delete_movement',
                           view_func=MovementDeleteView.as_view('delete_movement'))
    blueprint.add_url_rule('/save', endpoint='save_movement', view_func=MovementDetailView.as_view('save_movement'))

    blueprint.add_url_rule('/attachments/receipt/<int:movement_id>', endpoint='attachments',
                           view_func=AttachmentMovementListView.as_view('attachments'))
    blueprint.add_url_rule('/attachments/show/<int:id>', endpoint='show_attachment',
                           view_func=AttachmentMovementDetailView.as_view('show_attachment'))
    blueprint.add_url_rule('/attachments/order/<int:movement_id>/new', endpoint='new_attachment',
                           view_func=AttachmentMovementDetailView.as_view('new_attachment'))
    blueprint.add_url_rule('/attachments/delete/<int:id>', endpoint='delete_attachment',
                           view_func=AttachmentMovementDeleteView.as_view('delete_attachment'))
    blueprint.add_url_rule('/attachments/save', endpoint='save_attachment',
                           view_func=AttachmentMovementDetailView.as_view('save_attachment'))
    return blueprint
