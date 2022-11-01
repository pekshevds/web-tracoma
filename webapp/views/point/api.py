from flask import render_template, redirect, url_for

from webapp.db.point.fetchers import get_points
from webapp.db.point.changers import delete_point
from webapp.views.point.forms import PointForm
from webapp.views.common import BaseView


class PointView(BaseView):
    form_class = PointForm
    template_name = 'point_item.html'
    methods = ['GET', 'POST']

    def get_success_url(self):
        return url_for('point.points')

    @staticmethod
    def points_view():
        return render_template('point_list.html', points=get_points())

    @staticmethod
    def delete_point_view(point_id: int):
        if delete_point(id=point_id):
            return redirect(url_for('point.points'))
        return render_template("crud_error.html", content='error on mark point for deleting')
