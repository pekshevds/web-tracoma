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

    id = IntegerField(label="Id: ", validators=[DataRequired()], name="id", default=-1)
    title = StringField(label="Title: ", name="title", default="")
    storage_id = IntegerField(label="Storage: ", validators=[DataRequired()], name="storage")

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})


class AttachmentForm(ModelForm):
    class Meta:
        model = AttachmentReceiptOfCargo

    id = IntegerField(label="Id: ", validators=[DataRequired()], name="id", default=-1)
    receipt_id = IntegerField(label="Receipt_id: ", validators=[DataRequired()], name="receipt_id")

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})
