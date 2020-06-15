# Tuodaan Flask käyttöön
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)


if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ostoslista.db"
    app.config["SQLALCHEMY_ECHO"] = True


# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# kirjautuminen
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)



# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Luetaan tietokantataulujen sqlalchemy-mallit
from application.items import models
from application.categories import models
from application.lists import models
from application.auth import models
from application.purchases import models
from application.lists import user_list

from application.categories import views
from application.lists import views
from application.auth import views
from application.items import views
from application.purchases import views


from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Luodaan lopulta tarvittavat tietokantataulut
try:
    db.create_all()
except:
    pass
