from sqlalchemy.exc import SQLAlchemyError
from flask import render_template, redirect, url_for
from flask_views.edit import FormView
from flask_views.base import TemplateView
from webapp.db.common import db
from webapp.db.storage.fetchers import get_carriers, get_counteragents, get_storages
from webapp.db.point.fetchers import get_points


class DetailView(FormView):
    self_url_name = ""
    methods = ['GET', 'POST']
    model = None

    def get_self_url(self, id):
        return url_for(self.self_url_name, id=id)

    def initial_form_values(self, object: object):
        form = self.get_form()
        for key in form.data.keys():
            if hasattr(object, key):
                form[key].data = getattr(object, key)
        return form

    def initial_object_from_form_values(self, object: object, form, excluded_columns: list = ['is_deleted']):
        for key in form.data.keys():
            if key in excluded_columns:
                continue
            if hasattr(object, key):
                setattr(object, key, form[key].data)
        return object

    def get_object_by_id(self, id: int) -> object:
        object_class = self.model
        return object_class.query.filter(object_class.id == id).first()

    def pre_save(self, obj: object) -> None:
        pass

    def save_object(self, form) -> bool:
        object_class = self.model
        id = form.id.data
        if id:
            new_object = self.get_object_by_id(id=id)
            new_object = self.initial_object_from_form_values(new_object, form)
        else:
            new_object = object_class()
            form.populate_obj(new_object)
            new_object.id = None
        self.pre_save(new_object)
        db.session.add(new_object)
        try:
            db.session.commit()
        except (RuntimeError, SQLAlchemyError):
            return None
        return new_object

    def get_attachments(self, id: int):
        pass

    def get_context_data(self, **kwargs):
        id = kwargs.get("id", 0)
        kwargs['carriers'] = get_carriers()
        kwargs['counteragents'] = get_counteragents()
        kwargs['points'] = get_points()

        storages = get_storages()
        kwargs['shippers'] = storages
        kwargs['consignees'] = storages
        kwargs['storages'] = storages

        kwargs['attachments'] = self.get_attachments(id)
        return kwargs

    def get(self, *args, **kwargs):
        object = self.get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = self.initial_form_values(object)
        else:
            form = self.get_form()
        return render_template(self.template_name, form=form, **self.get_context_data(**kwargs))

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.validate_on_submit():
            obj = self.save_object(form)
            if obj:
                return redirect(self.get_self_url(id=obj.id))
        return render_template(self.template_name, form=form)


class ListView(TemplateView):
    template_name = ''

    def get_context_data(self, **kwargs):
        return kwargs

    def get(self, *args, **kwargs):
        return render_template(self.template_name, **self.get_context_data(**kwargs))

class DeleteView(TemplateView):
    success_url_name = ''

    def delete(self, id: int):
        pass

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        if self.delete(id=id):
            return redirect(url_for(self.success_url_name))
        return render_template("crud_error.html", content='error on mark for deleting')
