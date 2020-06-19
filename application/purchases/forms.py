from flask_wtf import FlaskForm
from wtforms import DecimalField, validators, SelectField


class AddNewPurchaseForm(FlaskForm):
    name = SelectField("Tuote", coerce=int)
    amount = DecimalField(
        "Määrä", default=1, validators=[validators.required()]
    )

    class Meta:
        csrf = False
