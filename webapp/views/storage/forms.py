from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, BooleanField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory
from webapp.db import Storage


ModelForm = model_form_factory(FlaskForm)


class StorageForm(ModelForm):
    class Meta:
        model = Storage

    id = IntegerField(label="Id: ", name="id")
    title = StringField(label="Title: ", validators=[DataRequired()], name="title", default="")
    is_internal = BooleanField(label="Internal: ", name="is_internal", default=False)
    is_employee = BooleanField(label="Employee: ", name="is_employee", default=False)
    kind = IntegerField(label="Kind: ", validators=[DataRequired()], name="kind", default=1)
    inn = StringField(label="INN: ", name="inn", default="")
    kpp = StringField(label="KPP: ", name="kpp", default="")
    weight = FloatField(label="Weight: ", name="weight", default=.0)
    volume = FloatField(label="Volume: ", name="volume", default=.0)

    submit = SubmitField("Save", render_kw={"class": "btn btn-primary"})
