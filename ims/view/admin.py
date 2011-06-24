from flask import Module, request, flash, url_for, redirect, \
     render_template, abort
from flaskext.sqlalchemy import SQLAlchemy
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
        admin = User('admin', '111111', 'admin@example.com')
        guest = User('guest', '222222', 'guest@example.com')
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

@mod.add_user('/add_user', methods = ['POST'])
@login_required
def add_user(name = None, password = None, email = None):
    if request.method == 'POST':
        username = form['username']
        password = form['password']
        email    = form['email']
    hash_pass = generate_password_hash(password, method='sha1', salt_length=8)
    user = User(name, hash_pass, email)
    try:
        db.session.add(user)
        db.session.commit()
    except:
        flash("add user failed", 'error')

@mod.add_user('/del_user', methods = ['POST'])
@login_required
def del_user():
    if request.method == 'POST':
        username = form['username']
    user = User.query.filter_by(username=username)
    try:
        db.session.remove(user)
        db.session.commit()
    except:
        flash("del user failed", 'error')


@mod.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        flash('Config saved.')
        return render_template('admin.html')
    else:
        return render_template('admin.html')
