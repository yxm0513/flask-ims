from flask import Module, request, flash, url_for, redirect, \
     render_template, abort
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.login import login_required
from werkzeug import generate_password_hash



mod = Module(__name__, url_prefix='/admin')

from ims.models import db, User, Todo
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
        db.session.add(guest)
    except:
        flash("init User table failed.", 'error')
    
    try:
        todo1 = Todo('check in code', 'modify reset')
        todo2 = Todo('talk with somebody', 'about cloud')
        db.session.add(todo1)
        db.session.add(todo2)
    except:
        flash("init Todo table failed.", 'error')

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
def add_user(name = None, password = None, email = None):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email    = request.form['email']
    hash_pass = generate_password_hash(password, method='sha1', salt_length=8)
    user = User(username, hash_pass, email)
    try:
        db.session.add(user)
        db.session.commit()
        flash("add user done.")
    except:
        flash("add user failed %s" % user.username, 'error')
    return redirect(url_for('index'))

@mod.route('/del_user', methods = ['POST'])
@login_required
def del_user():
    if request.method == 'POST':
        username = request.form['username']
    user = User.query.filter_by(username=username).first()
    try:
        db.session.delete(user)
        db.session.commit()
        flash("del user done.")
    except:
        flash("del user failed %s" % user.username, 'error')
    return redirect(url_for('index'))


@mod.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        flash('Config saved.')
        return render_template('admin.html')
    else:
        return render_template('admin.html')
