from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory
from webapp.db import ReceiptOfCargo
from webapp.db.receipt_of_cargo.models import AttachmentReceiptOfCargo


ModelForm = model_form_factory(FlaskForm)


class ReceiptForm(ModelForm):
    class Meta:
        model = ReceiptOfCargo

    id = IntegerField(label="Id: ", name="id")
    title = StringField(label="Title: ", name="title", default="")
    storage_id = IntegerField(label="Storage: ", validators=[DataRequired()], name="storage")
    cost = FloatField(label="Cost: ", name="cost", default=.0)

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})


class AttachmentForm(ModelForm):
    class Meta:
        model = AttachmentReceiptOfCargo

    id = IntegerField(label="Id: ", name="id")
    receipt_id = IntegerField(label="Receipt_id: ", validators=[DataRequired()], name="receipt_id")
    order_id = IntegerField(label="Order: ", validators=[DataRequired()], name="order")

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})
