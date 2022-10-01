from flask import render_template


def get_home_view():
    return render_template('index.html')


def get_about_view():
    return render_template('about.html')
