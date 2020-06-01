from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField(
        "Käyttäjänimi", validators=[validators.Length(min=3)]
    )
    password = PasswordField("Salasana", validators=[validators.Length(min=3)])

    class Meta:
        csrf = False


class SignUpForm(FlaskForm):
    name = StringField("Nimi", validators=[validators.Length(min=3)])
    username = StringField(
        "Käyttäjänimi", validators=[validators.Length(min=3)]
    )
    password = PasswordField("Salasana", validators=[validators.Length(min=3)])

    class Meta:
        csrf = False
