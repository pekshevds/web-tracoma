from flask import render_template, request, redirect, url_for

from webapp.db.point.fetchers import get_points, get_point_by_id
from webapp.db.point.changers import update_or_create_point, delete_point
from webapp.utils import prepare_point_values


def points_view():
    return render_template('point_list.html', points=get_points())


def point_view(point_id: int):
    return render_template('point_item.html', point=get_point_by_id(point_id=point_id))


def new_point_view():
    return render_template('point_item.html', point=None)


def save_point_view():
    id, title, short = prepare_point_values(request.values)    
    if update_or_create_point(point_id=id, title=title, short=short):
        return redirect(url_for('points'))
    return render_template("crud_error.html", content='error on create or update point info')


def delete_point_view(point_id: int):    
    if delete_point(point_id=point_id):
        return redirect(url_for('points'))
    return render_template("crud_error.html", content='error on mark point for deleting')