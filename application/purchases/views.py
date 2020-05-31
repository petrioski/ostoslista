from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app
from application import db
from application.purchases.models import Purchase
from application.items.models import Item
from application.purchases.forms import AddNewPurchaseForm
# from application.categories.models import Category

# TODO: formi itemille


@app.route("/lists/<list_id>/purchases/add_mode/<add_mode>")
@login_required
def purchases_index(list_id, add_mode):
    #add_mode = request.args.get('add_mode', default=0, type=int)
    print("listan id " + list_id)
    print(f"THIIIISIIS purchase index {add_mode}")
    return render_template("purchases/list_contents.html", purchases=get_all_purchases(list_id), list_id=list_id, form=get_purchase_form(), add_mode=add_mode)
    # return render_template("items/all_items.html")


def get_all_purchases(list_id):
    return Purchase.query.filter_by(list_id=list_id).order_by(Purchase.item_id).all()

def get_purchase_form():
    items = db.session.query(Item).all()
    form = AddNewPurchaseForm(request.form)
    item_selection = [(i.id, i.name) for i in items]
    form.name.choices = item_selection

    return form


@app.route("/lists/<list_id>/purchases/add/<add_mode>", methods=["GET", "POST"])
@login_required
def create_purchase(list_id, add_mode):
    print("TTTTTTTTTTT " + list_id)
    form = get_purchase_form()

    if request.method == "GET":
        return render_template("purchases/add_purchases.html", form=form, list_id = list_id, purchases=get_all_purchases(list_id), add_mode=add_mode)

    if request.method == "POST" and not form.validate_on_submit():
        return render_template("/purchases/add_purchases.html", form=form)

    new_item = Purchase(form.amount.data)
    new_item.item_id = form.name.data
    new_item.list_id = list_id

    db.session().add(new_item)
    db.session().commit()

    return redirect(url_for("create_purchase", list_id = list_id, add_mode=add_mode))


@app.route("/list/<list_id>/purchases/remove/<purchase_id>/add_mode/<add_mode>", methods=["POST"])
@login_required
def delete_purchase(list_id, purchase_id, add_mode):
    db.session.query(Purchase).filter_by(id=purchase_id).delete()
    db.session.commit()

    print(f"THIIIISIIS in delete {add_mode} ja vertailun tulos {add_mode == 1}")

    if add_mode == str(1):
        return redirect(url_for("create_purchase", list_id = list_id, add_mode=add_mode))

    return redirect(url_for("purchases_index", list_id = list_id, add_mode=add_mode))
