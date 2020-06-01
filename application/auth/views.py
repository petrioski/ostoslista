from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application import db
from application.auth.models import User
from application.auth.forms import LoginForm, SignUpForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit
    if request.method == "POST" and not form.validate_on_submit():
        return render_template("auth/loginform.html", form=form)

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data
    ).first()
    if not user:
        return render_template(
            "auth/loginform.html",
            form=form,
            error="No such username or password",
        )

    login_user(user)

    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/signup", methods=["GET", "POST"])
def auth_sign_up():
    if request.method == "GET":
        return render_template("auth/signup.html", form=SignUpForm())

    form = SignUpForm(request.form)

    if request.method == "POST" and not form.validate_on_submit():
        return render_template("auth/signup.html", form=form)

    name = form.name.data
    username = form.username.data
    password = form.password.data
    new_user = User(name, username, password)

    db.session().add(new_user)
    db.session().commit()

    return redirect(url_for("auth_login"))
