from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory
from webapp.db import Order
from webapp.db.order.models import Attachment


ModelForm = model_form_factory(FlaskForm)


class OrderForm(ModelForm):
    class Meta:
        model = Order

    id = IntegerField(label="Id: ", validators=[DataRequired()], name="id", default=-1)
    title = StringField(label="Title: ", name="title", default="")

    carrier_id = IntegerField(label="Carrier: ", validators=[DataRequired()], name="carrier")

    consignee_id = IntegerField(label="Consignee: ", validators=[DataRequired()], name="consignee")
    consignee_address = StringField(label="Consignee address: ", name="consignee_address", default="")
    consignee_contact_id = IntegerField(label="Consignee contact: ", name="consignee_contact", default=0)
    consignee_phone = StringField(label="Consignee phone: ", name="consignee_phone", default="")

    shipper_id = IntegerField(label="Shipper: ", validators=[DataRequired()], name="shipper")
    shipper_address = StringField(label="Shipper address: ", name="shipper_address", default="")
    shipper_contact_id = IntegerField(label="Shipper contact: ", name="shipper_contact", default=0)
    shipper_phone = StringField(label="Shipper phone: ", name="shipper_phone", default="")

    point_from_id = IntegerField(label="Point from: ", validators=[DataRequired()], name="point_from")
    point_to_id = IntegerField(label="Point to: ", validators=[DataRequired()], name="point_to")

    declared = FloatField(label="Declared: ", name="declared", default=.0)
    desc = StringField(label="Description: ", name="desc", default="")
    weight = FloatField(label="Weight: ", name="weight", default=.0)
    volume = FloatField(label="Volume: ", name="volume", default=.0)

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})


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
