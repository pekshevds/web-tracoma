from flask import render_template

def home_view():
    return render_template('index.html')


def about_view():
    return render_template('about.html')
