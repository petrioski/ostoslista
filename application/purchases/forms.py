from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, SelectField


class AddNewPurchaseForm(FlaskForm):
    name = SelectField("Tuote", coerce=int)
    amount = IntegerField("Määrä", default=1, validators=[validators.required()])

    class Meta:
        csrf = False


# class UpdateShoppingListForm(FlaskForm):
#     name = StringField("List name", [validators.Length(min=3)])
#     # done = BooleanField("Valmis")

#     class Meta:
#         csrf = False
