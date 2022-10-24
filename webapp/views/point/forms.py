from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class PointForm(FlaskForm):
    id = IntegerField(label="Id: ", validators=[DataRequired()], name="id", default=-1)
    title = StringField(label="Title: ", validators=[DataRequired()], name="title", default="")
    short = StringField(label="Short: ", validators=[DataRequired()], name="short", default="")
    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})
