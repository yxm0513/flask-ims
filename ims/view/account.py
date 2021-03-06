from flask import Module, redirect, request, \
    flash, url_for, session
from flaskext.login import  LoginManager, login_user, logout_user,\
        login_required, logout_user, UserMixin, AnonymousUser,\
        confirm_login, fresh_login_required, current_user
from ims.models import db, User
from ims.forms import LoginForm, RegisterForm
from ims.theme import render_template

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

login_manager = LoginManager()

login_manager.anonymous_user = Anonymous
login_manager.login_view = "account"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

from ims import app
login_manager.setup_app(app)

@login_manager.user_loader
def load_user(id):
    try:
        return LoginUser(int(id), User.query.get(id).username)
    except:
        return None

@login_manager.unauthorized_handler
def unauthorized():
    return render_template("account/unauthorized.html")


# URL

@mod.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        #remember = form.remember.data
        remember = 1
        user = User.query.filter_by(username = username).first()
        if not len(form.errors):
            if user and user.check_password(password):
                loginuser = LoginUser(user.id, user.username)
                if login_user(loginuser, remember=remember):
                    flash("Logged in successfully!")
                    return redirect(request.args.get('next') or url_for("general.index"))
                else:
                    flash("Sorry, but you could not log in.", 'error')
            else:
                flash("Incorrect username or password", 'error')
    return render_template("account/login.html", form = form)

@mod.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("general.index"))

@mod.route('/register', methods=['GET', 'POST'])
def register():
    """Registers the user."""
    form = RegisterForm(request.form)
    if not (current_user.is_anonymous()):
        flash("you are logined")
        return render_template('logout.html')
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        password2 = form.password2.data
        email = form.email.data
        if User.query.filter_by(username = username).first():
            flash('The username is already taken')
        elif cmp(password, password2) != 0:
            flash('password mismatched')
        else:
            user = User(username, None, email)
            user.set_password(password)
            try:
                user.store_to_db()
                return render_template('account/registerok.html')
            except:
                flash('You were register failed, pls contact %s for help.' % app.config['ADMIN'][1])
    else:
        return render_template('account/register.html', form = form)
    return render_template('account/register.html', form = form)
