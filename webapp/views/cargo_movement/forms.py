from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory
from webapp.db import CargoMovement
from webapp.db.cargo_movement.models import AttachmentCargoMovement


ModelForm = model_form_factory(FlaskForm)


class MovementForm(ModelForm):
    class Meta:
        model = CargoMovement

    id = IntegerField(label="Id: ", validators=[DataRequired()], name="id", default=-1)
    title = StringField(label="Title: ", name="title", default="")
    shipper_id = IntegerField(label="Shipper: ", validators=[DataRequired()], name="shipper_id")
    consignee_id = IntegerField(label="Consignee: ", validators=[DataRequired()], name="consignee_id")
    cost = FloatField(label="Cost: ", validators=[DataRequired()], name="cost", default=.0)

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})


class AttachmentForm(ModelForm):
    class Meta:
        model = AttachmentCargoMovement

    id = IntegerField(label="Id: ", validators=[DataRequired()], name="id", default=-1)
    movement_id = IntegerField(label="Movement_id: ", validators=[DataRequired()], name="movement_id")
    order_id = IntegerField(label="Order: ", validators=[DataRequired()], name="order")

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})
