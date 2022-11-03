from sqlalchemy.exc import SQLAlchemyError
from flask import render_template, redirect, url_for
from flask_views.edit import FormView
from webapp.db.common import db


class BaseView(FormView):
    success_url_name = ""
    methods = ['GET', 'POST']

    def get_success_url(self):
        return url_for(self.success_url_name)

    def initial_form_values(self, object: object):
        form = self.get_form()
        for key in form.data.keys():
            if hasattr(object, key):
                form[key].data = getattr(object, key)
        return form

    def initial_object_values(self, object: object, form, excluded_columns: list = ['is_deleted']):
        for key in form.data.keys():
            if key in excluded_columns:
                continue
            if hasattr(object, key):
                setattr(object, key, form[key].data)
        return object

    def get_object_by_id(self, id: int) -> object:
        object_class = self.form_class.Meta.model
        return object_class.query.filter(object_class.id == id).first()

    def save_object(self, form) -> bool:
        object_class = self.form_class.Meta.model
        id = form.id.data
        if id:
            new_object = self.get_object_by_id(id=id)
            new_object = self.initial_object_values(new_object, form)
        else:
            print(form.data)
            new_object = object_class()
            form.populate_obj(new_object)
            new_object.id = None
        db.session.add(new_object)
        try:
            db.session.commit()
        except (RuntimeError, SQLAlchemyError):
            return False
        return True

    def get(self, *args, **kwargs):
        object = self.get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = self.initial_form_values(object)
        else:
            form = self.get_form()
        return render_template(self.template_name, form=form)

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.validate_on_submit():
            if self.save_object(form):
                return redirect(self.get_success_url())
        return render_template(self.template_name, form=form)
