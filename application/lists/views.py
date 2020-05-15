from application import app
from application import db
from flask import redirect, render_template, request, request, url_for
from application.lists.models import List


@app.route("/lists", methods=["GET"])
def lists_index():
    return render_template("lists/list.html", lists = List.query.all())

@app.route("/lists/new/")
def lists_form():
    return render_template("lists/new.html")

@app.route("/lists/<list_id>/", methods=["POST"])
def lists_set_done(list_id):
    id = List.query.get(list_id)

    if id.valmis == False:
        id.valmis = True
    else:
        id.valmis = False

    db.session().commit()

    return redirect(url_for("lists_index"))

@app.route("/lists/", methods=["POST"])
def lists_create():
    shopping_list = List(request.form.get("name"))

    db.session().add(shopping_list)
    db.session().commit()

    return redirect(url_for("lists_index"))
