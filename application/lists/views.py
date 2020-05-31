from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app
from application import db
from application.lists.models import List
from application.lists.forms import CreateNewShoppingListForm
from application.lists.forms import UpdateShoppingListForm


@app.route("/lists", methods=["GET"])
@login_required
def lists_index():
    return render_template(
        "lists/list.html",
        lists=List.query.filter_by(account_id=current_user.id)
        .order_by(List.done, List.date_modified.desc())
        .all(),
    )


@app.route("/lists/new/")
@login_required
def lists_form():
    return render_template("lists/new.html", form=CreateNewShoppingListForm())


@app.route("/lists/<list_id>/", methods=["GET", "POST"])
@login_required
def lists_set_done(list_id):
    id = List.query.get(list_id)

    if id.done is False:
        id.done = True
    else:
        id.done = False

    db.session().commit()

    return redirect(url_for("lists_index"))


# TODO
@app.route("/lists/add/<list_id>/", methods=["GET", "POST"])
@login_required
def lists_add_items(list_id):
    id = List.query.get(list_id)
    print(f"id on {id}")

    return redirect(url_for("list_content"))


@app.route("/lists/", methods=["GET", "POST"])
@login_required
def create_list():
    form = CreateNewShoppingListForm(request.form)

    if not form.validate_on_submit():
        return render_template("/lists/new.html", form=form)

    shopping_list = List(form.name.data)
    shopping_list.account_id = current_user.id

    db.session().add(shopping_list)
    db.session().commit()

    return redirect(url_for("lists_index"))


# TODO: update list name
@app.route("/lists/update/<list_id>/", methods=["GET", "POST"])
@login_required
def lists_update_x(list_id):
    id = List.query.get(list_id)
    print(f"nimi {id.name} ja id {id.id}")
    form_u = UpdateShoppingListForm(request.form)

    if request.method == "GET":
        return render_template("/lists/update.html", form=form_u, list=id)

    if request.method == "POST" and not form_u.validate_on_submit():
        return render_template("/lists/update.html", form=form_u, list=id)

    id.name = form_u.name.data
    db.session().commit()

    return redirect(url_for("lists_index"))


@app.route("/lists/remove/<list_id>/", methods=["POST"])
@login_required
def delete_list(list_id):
    db.session.query(List).filter_by(id=list_id).delete()
    db.session.commit()

    return redirect(url_for("lists_index"))
