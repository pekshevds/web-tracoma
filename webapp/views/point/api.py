from flask import render_template, redirect, url_for

from webapp.db.point.fetchers import get_points
from webapp.db.point.changers import delete_point
from webapp.views.point.forms import PointForm
from webapp.views.common import BaseView
from flask_views.edit import FormView


class PointDetailView(BaseView):
    form_class = PointForm
    template_name = 'point_item.html'
    success_url_name = 'point.points'


class PointListView(FormView):
    template_name = 'point_list.html'

    def get(self, *args, **kwargs):
        return render_template('point_list.html', points=get_points())


class PointDeleteView(FormView):
    template_name = 'point_list.html'

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        if delete_point(id=id):
            return render_template('point_list.html', points=get_points())
        return render_template("crud_error.html", content='error on mark point for deleting')
