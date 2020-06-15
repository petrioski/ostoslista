from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

error_msg = "Vain kirjaimet, numerot tai '@, +, -' -merkit sallittu"
lengt_error = "Pituus väliltä 3-144 merkkiä"


class LoginForm(FlaskForm):
    username = StringField(
        "Käyttäjänimi",
        validators=[
            validators.Length(min=3, max=144, message=lengt_error),
            validators.Regexp(r"^[\w.-]+$"),
        ],
    )
    password = PasswordField(
        "Salasana",
        validators=[validators.Length(min=3, max=144, message=lengt_error)],
    )

    class Meta:
        csrf = False


class SignUpForm(FlaskForm):
    name = StringField(
        "Nimi",
        validators=[
            validators.Length(min=3, max=144, message=lengt_error),
            validators.Regexp(r"(\w+\s?)+"),
        ],
    )
    username = StringField(
        "Käyttäjänimi",
        validators=[
            validators.Length(min=3, max=144, message=lengt_error),
            validators.Regexp(
                r"^[\w.@+-]+$",
                message=error_msg,
            ),
        ],
    )
    password = PasswordField(
        "Salasana",
        validators=[
            validators.Length(min=3, max=144, message=lengt_error),
            validators.Regexp(r"^[\w.@+-]+$", message=error_msg),
        ],
    )

    class Meta:
        csrf = False
