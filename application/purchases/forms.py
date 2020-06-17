from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, SelectField


class AddNewPurchaseForm(FlaskForm):
    name = SelectField("Tuote", coerce=int)
    amount = IntegerField(
        "Määrä", default=1, validators=[validators.required()]
    )

    class Meta:
        csrf = False
