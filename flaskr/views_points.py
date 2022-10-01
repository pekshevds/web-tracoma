from flask import render_template, redirect, url_for
from flaskr.samples import get_points, get_point_by_id
from flaskr.changes import delete_point_by_id, update_point, add_point

def get_points_view():
    return render_template('point_list.html', points=get_points())

def get_new_point_view():
    return render_template('point_item.html', storage=None)


def get_point_view(point_id: int):
    point=get_point_by_id(point_id)
    return render_template('point_item.html', point=point)


def get_points_after_deleting_by_id(point_id: int):
    delete_point_by_id(point_id)
    return redirect(url_for('points'))


def get_points_after_create_update_by_id(point_id: int, title: str, short: str):
    if point_id:
        update_point(id=point_id, title=title, short=short)
    else:        
        add_point(title=title, short=short)

    return redirect(url_for('points'))