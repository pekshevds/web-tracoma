from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory
from webapp.db import Point


ModelForm = model_form_factory(FlaskForm)


class PointForm(ModelForm):
    class Meta:
        model = Point

    id = IntegerField(label="Id: ", name="id")
    title = StringField(label="Title: ", validators=[DataRequired()], name="title", default="")
    short = StringField(label="Short: ", name="short", default="")

    latitude = FloatField(label="Latitude: ", name="latitude", default=.0)
    longitude = FloatField(label="longitude: ", name="longitude", default=.0)

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"}, name='save')
