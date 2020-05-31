from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField


class CreateNewItemForm(FlaskForm):
    name = StringField("Tuotteen nimi", [validators.Length(min=3)])
    unit_type = StringField("Mittayksikkö", [validators.Length(min=3)])
    category = SelectField("Kategoria", coerce=int)

    class Meta:
        csrf = False


# class UpdateShoppingListForm(FlaskForm):
#     name = StringField("List name", [validators.Length(min=3)])
#     # done = BooleanField("Valmis")

#     class Meta:
#         csrf = False
