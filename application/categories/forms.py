from flask_wtf import FlaskForm
from wtforms import StringField

class TaskForm(FlaskForm):
    name = StringField("Category name")

    class Meta:
        csrf = False