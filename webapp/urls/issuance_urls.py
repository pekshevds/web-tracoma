from flask.blueprints import Blueprint
from webapp.views.issuance_of_cargo import (IssuanceDetailView, IssuanceListView, IssuanceDeleteView,
                                            AttachmentIssuanceDetailView, AttachmentIssuanceListView,
                                            AttachmentIssuanceDeleteView)


def get_issuance_blueprints():
    blueprint = Blueprint(name='issuance', import_name='issuance', url_prefix='/issuances')
    blueprint.add_url_rule('/', endpoint='issuances', view_func=IssuanceListView.as_view('issuances'))
    blueprint.add_url_rule('/show/<int:id>', endpoint='show_issuance',
                           view_func=IssuanceDetailView.as_view('show_issuance'))
    blueprint.add_url_rule('/new', endpoint='new_issuance', view_func=IssuanceDetailView.as_view('new_issuance'))
    blueprint.add_url_rule('/delete/<int:id>', endpoint='delete_issuance',
                           view_func=IssuanceDeleteView.as_view('delete_issuance'))
    blueprint.add_url_rule('/save', endpoint='save_issuance', view_func=IssuanceDetailView.as_view('save_issuance'))

    blueprint.add_url_rule('/attachments/issuance/<int:issuance_id>', endpoint='attachments',
                           view_func=AttachmentIssuanceListView.as_view('attachments'))
    blueprint.add_url_rule('/attachments/show/<int:id>', endpoint='show_attachment',
                           view_func=AttachmentIssuanceDetailView.as_view('show_attachment'))
    blueprint.add_url_rule('/attachments/order/<int:issuance_id>/new', endpoint='new_attachment',
                           view_func=AttachmentIssuanceDetailView.as_view('new_attachment'))
    blueprint.add_url_rule('/attachments/delete/<int:id>', endpoint='delete_attachment',
                           view_func=AttachmentIssuanceDeleteView.as_view('delete_attachment'))
    blueprint.add_url_rule('/attachments/save', endpoint='save_attachment',
                           view_func=AttachmentIssuanceDetailView.as_view('save_attachment'))
    return blueprint
