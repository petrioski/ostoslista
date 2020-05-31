from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators


class CreateNewShoppingListForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3)])
    # done = BooleanField("Valmis")

    class Meta:
        csrf = False


class UpdateShoppingListForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3)])
    # done = BooleanField("Valmis")

    class Meta:
        csrf = False
