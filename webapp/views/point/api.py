from flask import render_template, redirect, url_for

from webapp.db.point.fetchers import get_points, get_point_by_id
from webapp.db.point.changers import delete_point, save_point
from webapp.views.point.forms import PointForm
from flask_views.edit import FormView


class PointView(FormView):
    form_class = PointForm
    template_name = 'point_item.html'
    methods = ['GET', 'POST']

    def get_success_url(self):
        return url_for('point.points')

    def get(self, *args, **kwargs):
        form = self.get_form()

        point_id = kwargs.get("point_id", 0)
        point = get_point_by_id(id=point_id)
        if point:
            for key in form.data.keys():
                if hasattr(point, key):
                    form[key].data = getattr(point, key)
        return render_template('point_item.html', form=form)

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.validate_on_submit():
            if save_point(form):
                return redirect(self.get_success_url())
        return render_template('point_item.html', form=form)

    @staticmethod
    def points_view():
        return render_template('point_list.html', points=get_points())

    @staticmethod
    def delete_point_view(point_id: int):
        if delete_point(id=point_id):
            return redirect(url_for('point.points'))
        return render_template("crud_error.html", content='error on mark point for deleting')
