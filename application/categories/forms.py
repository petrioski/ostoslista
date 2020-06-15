from flask_wtf import FlaskForm
from wtforms import StringField, validators


class CreateNewCategoryForm(FlaskForm):
    name = StringField("Tuotekategoria:", [validators.Length(min=3, max=500)])

    class Meta:
        csrf = False
