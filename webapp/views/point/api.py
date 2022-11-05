from flask import render_template, redirect, url_for

from webapp.db.point.models import Point
from webapp.db.point.fetchers import get_points
from webapp.db.point.changers import delete_point
from webapp.views.point.forms import PointForm
from webapp.views.common import DetailView, ListView, DeleteView


class PointDetailView(DetailView):
    form_class = PointForm
    template_name = 'point_item.html'
    self_url_name = 'point.show_point'
    model = Point


class PointListView(ListView):
    template_name = 'point_list.html'

    def get_context_data(self, **kwargs):
        kwargs['points'] = get_points()
        return kwargs


class PointDeleteView(DeleteView):
    success_url_name = 'point.points'

    def delete(self, id: int):
        return delete_point(id)
