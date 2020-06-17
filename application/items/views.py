from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app
from application import db
from application.items.models import Item
from application.categories.models import Category
from application.items.forms import CreateNewItemForm


@app.route("/items")
@login_required
def items_index():
    return render_template("items/all_items.html", items=Item.query.all())


@app.route("/items/add", methods=["GET", "POST"])
@login_required
def create_item():
    categories = db.session.query(Category).all()
    form = CreateNewItemForm(request.form)
    category_selection = [(i.id, i.name) for i in categories]
    form.category.choices = category_selection

    if not form.validate_on_submit():
        return render_template("/items/new.html", form=form)

    new_item = Item(form.name.data)
    new_item.unit_type = form.unit_type.data
    new_item.category_id = form.category.data

    db.session().add(new_item)
    db.session().commit()

    return redirect(url_for("items_index"))


@app.route("/items/update/<item_id>/", methods=["GET", "POST"])
@login_required
def update_item(item_id):
    categories = db.session.query(Category).all()
    form = CreateNewItemForm(request.form)
    category_selection = [(i.id, i.name) for i in categories]
    form.category.choices = category_selection

    old_item = Item.query.get(item_id)

    if request.method == "GET":
        form.name.data = old_item.name
        form.unit_type.data = old_item.unit_type
        return render_template("/items/update.html", form=form, item=old_item)

    if request.method == "POST" and not form.validate_on_submit():
        return render_template("/items/update.html", form=form)

    old_item.name = form.name.data
    old_item.unit_type = form.unit_type.data
    old_item.category_id = form.category.data

    db.session().commit()

    return redirect(url_for("items_index"))


@app.route("/items/remove/<item_id>/", methods=["POST"])
@login_required
def delete_item(item_id):
    db.session.query(Item).filter_by(id=item_id).delete()
    db.session.commit()

    return redirect(url_for("items_index"))
