from flask import render_template, redirect, url_for

from webapp.db.storage.models import Storage
from webapp.db.storage.fetchers import get_storages, get_storages_by_kind
from webapp.db.storage.changers import delete_storage
from webapp.views.storage.forms import StorageForm
from webapp.views.common import DetailView, ListView, DeleteView
from flask_views.base import TemplateView


class StorageDetailView(DetailView):
    form_class = StorageForm
    template_name = 'storage_item.html'
    self_url_name = 'storage.show_storage'
    model = Storage

    def get(self, *args, **kwargs):
        object = super().get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = super().initial_form_values(object)
        else:
            form = self.get_form()
            form.kind.data = kwargs.get("storage_kind", 2)
        return render_template(self.template_name, form=form)


class StorageListView(ListView):
    template_name = 'storage_list.html'

    def get_context_data(self, **kwargs):

        kwargs['storages'] = get_storages()
        storage_kind = kwargs.get("storage_kind", 0)
        if storage_kind:
            kwargs['storages'] = get_storages_by_kind(kind=storage_kind)
        return kwargs

class StorageDeleteView(DeleteView):
    success_url_name = 'storage.storages'

    def delete(self, id: int):
        return delete_storage(id)
