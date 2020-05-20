from flask import redirect, render_template, request, request, url_for
from flask_login import login_required

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

# @app.route("/lists/new/")
# def lists_form():
#     return render_template("lists/new.html")

@app.route("/lists/<list_id>/", methods=["POST"])
@login_required
def lists_set_done(list_id):
    id = List.query.get(list_id)

    if id.valmis == False:
        id.valmis = True
    else:
        id.valmis = False

    db.session().commit()

    return redirect(url_for("lists_index"))

@app.route("/lists/", methods=["GET","POST"])
@login_required
def lists_create():
    # shopping_list = List(request.form.get("name"))
    form = TaskForm(request.form)

    if not form.validate_on_submit():
        return render_template("/lists/new.html", form = form)

    shopping_list = List(form.name.data)
    shopping_list.valmis = form.valmis.data

    db.session().add(shopping_list)
    db.session().commit()

    return redirect(url_for("lists_index"))
