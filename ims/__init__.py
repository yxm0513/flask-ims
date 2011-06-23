import os, sys
import setting
from functools import wraps

from flask import Flask, render_template
from flaskext.debugtoolbar import DebugToolbarExtension


###################### App Start #######################
app = Flask(__name__)

# debug tool
toolbar = DebugToolbarExtension(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("image/favicon.ico")


from models import db, User, Todo
# database
@app.route("/initdb")
def initdb():
	db.create_all()
	admin = User('admin', '111111', 'admin@example.com')
	guest = User('guest', '222222', 'guest@example.com')
	db.session.add(admin)
	db.session.add(guest)
	todo1 = Todo('check in code', 'modify reset')
	todo2 = Todo('talk with somebody', 'about cloud')
	db.session.add(todo1)
	db.session.add(todo2)
	db.session.commit()
	return "init ok"

@app.route("/dropdb")
def dropdb():
	db.drop_all()
	return "drop ok"

# add modules
from view import login
from view import general
from view import todo

app.register_module(login.mod)
app.register_module(general.mod)
app.register_module(todo.mod)

