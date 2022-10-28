from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory
from webapp.db import IssuanceOfCargo
from webapp.db.issuance_of_cargo.models import AttachmentIssuanceOfCargo


ModelForm = model_form_factory(FlaskForm)


class IssuanceForm(ModelForm):
    class Meta:
        model = IssuanceOfCargo

    id = IntegerField(label="Id: ", validators=[DataRequired()], name="id", default=-1)
    title = StringField(label="Title: ", name="title", default="")
    storage_id = IntegerField(label="Storage: ", validators=[DataRequired()], name="storage")
    cost = FloatField(label="Cost: ", name="cost", default=.0)

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})


class AttachmentForm(ModelForm):
    class Meta:
        model = AttachmentIssuanceOfCargo

    id = IntegerField(label="Id: ", validators=[DataRequired()], name="id", default=-1)
    issuance_id = IntegerField(label="Issuance_id: ", validators=[DataRequired()], name="issuance_id")
    order_id = IntegerField(label="Order: ", validators=[DataRequired()], name="order")

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})
