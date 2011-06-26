from flask import Module, request, flash, url_for, redirect, \
     render_template, abort
from ims.models import db, Todo
from flaskext.login import login_required


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
    for todo in Todo.query.all():
        todo.done = ('done.%d' % todo.id) in request.form
        if ('del.%d' % todo.id) in request.form:
            todo.delete_from_db()
    flash('Updated status')
    return redirect(url_for('index'))
