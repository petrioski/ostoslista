from flask import redirect, render_template, request, request, url_for
from flask_login import login_required, current_user

from application import app
from application import db
from application.lists.models import List
from application.lists.forms import TaskForm


@app.route("/lists", methods=["GET"])
@login_required
def lists_index():
    return render_template("lists/list.html", lists = List.query.all())


@app.route("/lists/new/")
@login_required
def lists_form():
    return render_template("lists/new.html", form = TaskForm())


@app.route("/lists/<list_id>/", methods=["POST"])
@login_required
def lists_set_done(list_id):
    id = List.query.get(list_id)

    if id.done == False:
        id.done = True
    else:
        id.done = False

    db.session().commit()

    return redirect(url_for("lists_index"))

@app.route("/lists/", methods=["GET","POST"])
@login_required
def lists_create():
    form = TaskForm(request.form)

    if not form.validate_on_submit():
        return render_template("/lists/new.html", form = form)

    shopping_list = List(form.name.data)
    shopping_list.done = form.done.data
    shopping_list.account_id = current_user.id

    db.session().add(shopping_list)
    db.session().commit()

    return redirect(url_for("lists_index"))
