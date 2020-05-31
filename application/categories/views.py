from application import app
from application import db
from flask import redirect, render_template, request, request, url_for
from application.categories.models import Category
from application.categories.forms import CreateNewCategoryForm
from flask_login import login_required, current_user


@app.route("/categories", methods=["GET"])
@login_required
def categories_index():
    return render_template("categories/list.html", categories = Category.query.all())

# @app.route("/categories/new/")
# def categories_form():
#     return render_template("categories/new.html")

@app.route("/categories/", methods=["GET", "POST"])
@login_required
def create_category():
    form = CreateNewCategoryForm(request.form)

    if request.method == "GET":
        return render_template("categories/new.html", form=form)


    if request.method == "POST" and not form.validate_on_submit():
        return render_template("categories/new.html", form=form)

    cat = Category(request.form.get("name"))

    db.session().add(cat)
    db.session().commit()

    return redirect(url_for("categories_index"))

@app.route("/categories/new/")
def categories_form():
    return render_template("categories/new.html", form = TaskForm())
