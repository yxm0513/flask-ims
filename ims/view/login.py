from flask import Module, render_template, redirect
from flaskext.login import  login_user, logout_user

mod = Module(__name__)

# URL
@mod.route('/login', methods=["GET", "POST"])
def login():
#form = LoginForm()
#    if form.validate_on_submit():
        login_user(user)
        flash("Logged in successfully.")
#return redirect(request.args.get("next") or url_for("index"))
#return render_template('login.html', form=form)
        return render_template('login.html')



@mod.route("/logout")
#@login_required
def logout():
    logout_user()
    return redirect("index")
