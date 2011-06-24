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

# add modules

from view import login
from view import admin
from view import general
from view import todo

app.register_module(login.mod)
app.register_module(admin.mod)
app.register_module(general.mod)
app.register_module(todo.mod, url_prefix='/todo')
