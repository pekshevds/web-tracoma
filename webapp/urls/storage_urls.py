from flask.blueprints import Blueprint
from webapp.views.storage import StorageDetailView, StorageListView, StorageDeleteView


def get_storage_blueprints():
    blueprint = Blueprint(name='storage', import_name='storage', url_prefix='/storages')
    blueprint.add_url_rule('/', endpoint='storages', view_func=StorageListView.as_view('storages'))
    blueprint.add_url_rule('/kind/<int:storage_kind>', endpoint='storages_by_kind',
                           view_func=StorageListView.as_view('storages_by_kind'))
    blueprint.add_url_rule('/show/<int:id>', endpoint='show_storage',
                           view_func=StorageDetailView.as_view('show_storage'))
    blueprint.add_url_rule('/new/<int:storage_kind>', endpoint='new_storage',
                           view_func=StorageDetailView.as_view('new_storage'))
    blueprint.add_url_rule('/delete/<int:id>', endpoint='delete_storage',
                           view_func=StorageDeleteView.as_view('delete_storage'))
    blueprint.add_url_rule('/save', view_func=StorageDetailView.as_view('save_storage'))
    return blueprint
