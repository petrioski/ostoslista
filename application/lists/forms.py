from flask_wtf import FlaskForm
from wtforms import StringField, validators


class CreateNewShoppingListForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3, max=500)])

    class Meta:
        csrf = False


class UpdateShoppingListForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3, max=500)])

    class Meta:
        csrf = False
