import os, sys
import setting
from functools import wraps

from flask import Flask, render_template
from flaskext.debugtoolbar import DebugToolbarExtension


###################### App Start #######################
app = Flask(__name__)

# debug tool
toolbar = DebugToolbarExtension(app)

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("image/favicon.ico")


from models import db, User
# database
@app.route("/initdb")
def initdb():
	db.create_all()
	admin = User('admin', 'admin@example.com')
	guest = User('guest', 'guest@example.com')
	db.session.add(admin)
	db.session.add(guest)
	db.session.commit()
	return "init ok"

@app.route("/dropdb")
def dropdb():
	db.drop_all()	
	return "drop ok"

# add modules
from view import login
from view import general

app.register_module(login.mod)
app.register_module(general.mod)

