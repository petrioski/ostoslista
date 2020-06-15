from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField


class CreateNewItemForm(FlaskForm):
    name = StringField("Tuotteen nimi", [validators.Length(min=3, max=500)])
    unit_type = StringField(
        "Mittayksikkö", [validators.Length(min=3, max=144)]
    )
    category = SelectField("Kategoria", coerce=int)

    class Meta:
        csrf = False
