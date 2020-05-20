from application import app
from application import db
from flask import redirect, render_template, request, request, url_for
from application.categories.models import Category
from application.categories.forms import TaskForm


@app.route("/categories", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", categories = Category.query.all())

# @app.route("/categories/new/")
# def categories_form():
#     return render_template("categories/new.html")

@app.route("/categories/", methods=["POST"])
def categories_create():
    cat = Category(request.form.get("name"))

    db.session().add(cat)
    db.session().commit()

    return redirect(url_for("categories_index"))

@app.route("/categories/new/")
def categories_form():
    return render_template("categories/new.html", form = TaskForm())