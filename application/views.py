from flask import render_template
from application import app
from flask_login import current_user
from application.lists.views import lists_index

@app.route("/")
def index():
    if current_user.is_authenticated:
        return lists_index()
    else:
        return render_template("index.html")
