from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory
from webapp.db import Attachment


ModelForm = model_form_factory(FlaskForm)


class AttachmentForm(ModelForm):
    class Meta:
        model = Attachment

    id = IntegerField(label="Id: ", validators=[DataRequired()], name="id", default=-1)
    order_id = IntegerField(label="Order_id: ", validators=[DataRequired()], name="order_id")

    weight = FloatField(label="Weight: ", name="weight", default=.0)
    volume = FloatField(label="Volume: ", name="volume", default=.0)
    height = FloatField(label="Height: ", name="height", default=.0)
    width = FloatField(label="Width: ", name="width", default=.0)
    depth = FloatField(label="Depth: ", name="depth", default=.0)

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})
