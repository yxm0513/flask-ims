from flask import Module, request, flash, url_for, redirect, \
     render_template, abort
from flaskext.sqlalchemy import SQLAlchemy
from ims.models import db, Todo
from flaskext.login import login_required


mod = Module(__name__)


@mod.route('/todo')
def show_all():
    return render_template('todo/show_all.html',
        todos=Todo.query.order_by(Todo.pub_date.desc()).all()
    )


@mod.route('/todo/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        if not request.form['title']:
            flash('Title is required', 'error')
        elif not request.form['text']:
            flash('Text is required', 'error')
        else:
            todo = Todo(request.form['title'], request.form['text'])
            db.session.add(todo)
            db.session.commit()
            flash(u'Todo item was successfully created')
            return redirect(url_for('show_all'))
    return render_template('todo/new.html')


@mod.route('/todo/do', methods=['POST'])
@login_required
def do():
    for todo in Todo.query.all():
        todo.done = ('done.%d' % todo.id) in request.form
        if ('del.%d' % todo.id) in request.form:
            db.session.delete(todo)
    flash('Updated status')
    db.session.commit()
    return redirect(url_for('show_all'))
