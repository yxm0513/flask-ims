from flask import Module, request, flash, url_for, redirect, \
     render_template, abort
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.login import login_required
from werkzeug import generate_password_hash



mod = Module(__name__, url_prefix='/admin')

from ims.models import db, User, Todo
from ims.forms import AddUserForm, RemoveUserForm

# database
@mod.route('/initdb')
def initdb():
    try:
        db.create_all()
    except:
        db.drop_all()
    # add some records
    try:
        admin_pass = generate_password_hash('admin', method='sha1', salt_length=8)
        guest_pass = generate_password_hash('guest', method='sha1', salt_length=8)
        admin = User('admin', admin_pass, 'admin@example.com')
        guest = User('guest', guest_pass, 'guest@example.com')
        db.session.add(admin)
        flash("user admin added", 'message')
        db.session.add(guest)
        flash("user admin added", 'message')
    except:
        flash("create User table failed.", 'error')
    
    try:
        todo1 = Todo('check in code', 'modify reset')
        todo2 = Todo('talk with somebody', 'about cloud')
        db.session.add(todo1)
        flash("todo #1 added", 'message')
        db.session.add(todo2)
        flash("todo #2 added", 'message')
    except:
        flash("create Todo table failed.", 'error')

    try:
        db.session.commit()
        flash("database commit ok")
    except:
        flash("database commit failed.", 'error')
    
    return redirect(url_for('index'))

@mod.route('/dropdb')
def dropdb():
    db.drop_all()
    flash("drop database ok")
    return redirect(url_for('index'))

@mod.route('/add_user', methods = ['POST'])
@login_required
def add_user():
    add_form = AddUserForm(request.form)
    remove_form = RemoveUserForm(request.form)
    if request.method == 'POST' and add_form.validate_on_submit():
        username = add_form.username.data
        password = add_form.password.data
        email    = add_form.email.data
        if User.query.filter_by(username = username).first():
            flash('The username is already taken')
        hash_pass = generate_password_hash(password, method='sha1', salt_length=8)
        user = User(username, hash_pass, email)
        try:
            db.session.add(user)
            db.session.commit()
            flash("add user %s done." % user.username)
        except:
            flash("add user failed %s" % user.username, 'error')
    return render_template('admin/index.html', add_form = add_form, remove_form = remove_form)


@mod.route('/del_user', methods = ['POST'])
@login_required
def del_user():
    add_form = AddUserForm(request.form)
    remove_form = RemoveUserForm(request.form)
    if request.method == 'POST' and remove_form.validate_on_submit():
        username = remove_form.username.data
        user = User.query.filter_by(username = username).first()
        if not user:
            flash('The username has not taken')
        else:
            try:
                db.session.delete(user)
                db.session.commit()
                flash("del user %s done." % user.username)
            except:
                flash("del user failed %s" % user.username, 'error')
    return render_template('admin/index.html', add_form = add_form, remove_form = remove_form)

@mod.route('/', methods = ['GET', 'POST'])
def index():
    add_form = AddUserForm(request.form)
    remove_form = RemoveUserForm(request.form)
    if request.method == 'POST':
        flash('Config saved.')
        return render_template('admin/index.html', add_form = add_form, remove_form = remove_form)
    else:
        return render_template('admin/index.html', add_form = add_form, remove_form = remove_form)
