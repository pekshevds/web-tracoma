from flask import render_template, redirect, url_for

from webapp.db.storage.fetchers import get_storages, get_storages_by_kind
from webapp.db.storage.changers import delete_storage
from webapp.views.storage.forms import StorageForm
from webapp.views.common import BaseView
from flask_views.base import TemplateView


class StorageDetailView(BaseView):
    form_class = StorageForm
    template_name = 'storage_item.html'
    success_url_name = 'storage.storages'

    def get(self, *args, **kwargs):
        object = super().get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = super().initial_form_values(object)
        else:
            form = self.get_form()
            form.kind.data = kwargs.get("storage_kind", 2)
        return render_template(self.template_name, form=form)


class StorageListView(TemplateView):
    template_name = 'storage_list.html'

    def get(self, *args, **kwargs):
        storage_kind = kwargs.get("storage_kind", 0)
        if storage_kind:
            return render_template(self.template_name, storages=get_storages_by_kind(kind=storage_kind))
        return render_template(self.template_name, storages=get_storages())


class StorageDeleteView(TemplateView):
    success_url_name = 'storage.storages'

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        if delete_storage(id=id):
            return redirect(url_for(self.success_url_name))
        return render_template("crud_error.html", content='error on mark point for deleting')
