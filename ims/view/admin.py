from flask import Module, request, flash, url_for, redirect, \
     render_template, abort
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.login import login_required
from werkzeug import generate_password_hash



mod = Module(__name__, url_prefix='/admin')

from ims.models import db, User, Todo, Wiki
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
        # save them into database
        admin.store_to_db()
        flash("user admin added")
        guest.store_to_db()
        flash("user guest added")
    except:
        flash("create User table failed.", 'error')
    
    try:
        todo1 = Todo('check in code', 'modify reset')
        todo2 = Todo('talk with somebody', 'about cloud')
        todo1.store_to_db()
        flash("todo #1 added")
        todo2.store_to_db()
        flash("todo #2 added")
    except:
        flash("create Todo table failed.", 'error')
    
    try:
        wiki1 = Wiki('MainPage', 'wikitest')
        wiki2 = Wiki('Sandbox', 'wikitest')
        wiki1.store_to_db()
        flash("wiki #1 added")
        wiki2.store_to_db()
        flash("wiki #2 added")
    except:
        flash("create Wiki table failed.", 'error')
    return redirect(url_for('index'))

@mod.route('/dropdb')
def dropdb():
    db.drop_all()
    flash("drop database ok")
    return redirect(url_for('index'))

@mod.route('/adduser', methods = ['GET', 'POST'])
@login_required
def adduser():
    add_form = AddUserForm(request.form)
    if request.method == 'POST' and add_form.validate_on_submit():
        username = add_form.username.data
        password = add_form.password.data
        email    = add_form.email.data
        if User.query.filter_by(username = username).first():
            flash('The username is already taken')
        hash_pass = generate_password_hash(password, method='sha1', salt_length=8)
        user = User(username, hash_pass, email)
        try:
            user.store_to_db()
            flash("add user %s done." % user.username)
        except:
            flash("add user failed %s" % user.username, 'error')
    return render_template('admin/adduser.html', add_form = add_form)


@mod.route('/deluser', methods = ['GET', 'POST'])
@login_required
def deluser():
    remove_form = RemoveUserForm(request.form)
    if request.method == 'POST' and remove_form.validate_on_submit():
        username = remove_form.username.data
        user = User.query.filter_by(username = username).first()
        if not user:
            flash('The username has not taken')
        else:
            try:
                user.delete_from_db()
                flash("del user %s done." % user.username)
            except:
                flash("del user failed %s" % user.username, 'error')
    return render_template('admin/deluser.html', remove_form = remove_form)

@mod.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('admin/index.html')

@mod.route('/listuser', methods = ['GET', 'POST'])
def listuser():
    return render_template('admin/listuser.html')

@mod.route('/addtodo', methods = ['GET', 'POST'])
def addtodo():
    return render_template('admin/addtodo.html')

@mod.route('/delodo', methods = ['GET', 'POST'])
def deltodo():
    return render_template('admin/deltodo.html')

@mod.route('/listtodo', methods = ['GET', 'POST'])
def listtodo():
    return render_template('admin/listtodo.html')
