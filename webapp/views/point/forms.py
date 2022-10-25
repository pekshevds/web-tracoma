from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory
from webapp.db import Point


ModelForm = model_form_factory(FlaskForm)


class PointForm(ModelForm):
    class Meta:
        model = Point

    id = IntegerField(label="Id: ", name="id", default=0)
    title = StringField(label="Title: ", validators=[DataRequired()], name="title", default="")
    short = StringField(label="Short: ", name="short", default="")
    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"}, name='save')
