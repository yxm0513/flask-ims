from flask import Module, request, flash, url_for, redirect, \
     abort
from ims.models import db, Todo
from flaskext.login import login_required

from ims.theme import render_template

mod = Module(__name__)


@mod.route('/')
def index():
    return render_template('todo/index.html',
        todos=Todo.query.order_by(Todo.pub_date.desc()).all()
    )

@mod.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        if not request.form['title']:
            flash('Title is required', 'error')
        elif not request.form['text']:
            flash('Text is required', 'error')
        else:
            todo = Todo(request.form['title'], request.form['text'])
            todo.store_to_db()
            flash(u'Todo item was successfully created')
            return redirect(url_for('index'))
    return render_template('todo/new.html')


@mod.route('/do', methods=['POST'])
@login_required
def do():
    if request.method == 'POST':
        if 'done' in request.form:
            for key in request.form.keys():
               if key[0:2] == 'S.':
                   todo = Todo.query.get(key[2])
                   if todo.done:
                       todo.done = False
                   else:
                       todo.done = True
                   todo.update_to_db()
        if 'delete' in request.form:
            for key in request.form.keys():
               if key[0:2] == 'S.':
                   todo = Todo.query.get(key[2])
                   todo.delete_from_db()
    flash('Updated')
    return redirect(url_for('index'))
