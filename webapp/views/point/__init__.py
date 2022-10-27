from flask import render_template, redirect, url_for

from webapp.db.point.fetchers import get_points, get_point_by_id
from webapp.db.point.changers import delete_point, save_point
from webapp.views.point.forms import PointForm
from webapp.db.common import db
from webapp.db import Point


def points_view():
    return render_template('point_list.html', points=get_points())


def point_view(point_id: int):
    point = get_point_by_id(id=point_id)
    form = PointForm(obj=point)

    return render_template('point_item.html', form=form)


def new_point_view():
    form = PointForm()
    return render_template('point_item.html', form=form)


def save_point_view():
    form = PointForm()
    if form.validate_on_submit():
        if save_point(form):
            return redirect(url_for("points"))
        return render_template("crud_error.html", content='error on create or update point info')
    return render_template("crud_error.html", content='error on validation')


def delete_point_view(point_id: int):
    if delete_point(id=point_id):
        return redirect(url_for('points'))
    return render_template("crud_error.html", content='error on mark point for deleting')
