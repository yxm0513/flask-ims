from flask import Module, render_template, redirect, request, \
    flash, url_for
from flaskext.login import  LoginManager, login_user, logout_user,\
        login_required, logout_user, UserMixin, AnonymousUser,\
        confirm_login, fresh_login_required
from ims.models import db, User

mod = Module(__name__)

class LoginUser(UserMixin):
    def __init__(self, id, name=None, active=True):
        self.id = id
        self.name = name
        self.active = active
    
    def is_active(self):
        return self.active

class Anonymous(AnonymousUser):
    name = u"Anonymous"


USERS = {
    1: LoginUser(u"Notch", 1),
    2: LoginUser(u"Steve", 2),
    3: LoginUser(u"Creeper", 3, False),
}

USER_NAMES = dict((u.name, u) for u in USERS.itervalues())

login_manager = LoginManager()

login_manager.anonymous_user = Anonymous
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

@login_manager.user_loader
def load_user(id):
	return USERS.get(int(id))

from ims import app
login_manager.setup_app(app)

def add_user(name = None, password = None, email = None):
    user = User(name, password, email)
    db.session.add(user)
    db.session.commit()
    app.logger.debug('add user:%s ok'% user.name)
    
def del_user(name = None, password = None, email = None):
    user = User(name, password, email)
    db.session.drop(user)
    db.session.commit()
    app.logger.debug('del user:%s ok'% user.name)

# URL

@mod.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST" and "username" in request.form:
        username = request.form["username"]
        for user in User.query.all():
            if username == user.username:
                remember = request.form.get("remember", "no") == "yes"
                if login_user(username, remember=remember):
                    flash("Logged in successfully!")
                    return redirect(request.args.get("next") or url_for("general.index"))
                else:
                    flash("Sorry, but you could not log in.")
        else:
            flash(u"Invalid username.")
    return render_template("login.html")



@mod.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("general.index"))
