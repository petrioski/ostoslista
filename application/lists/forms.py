from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class TaskForm(FlaskForm):
    name = StringField("List name", [validators.Length(min=3)])
    done = BooleanField("Valmis")

    class Meta:
        csrf = False