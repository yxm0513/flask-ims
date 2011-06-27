import os, sys
import setting
from functools import wraps

from flask import Flask, render_template, jsonify
from flaskext.debugtoolbar import DebugToolbarExtension

###################### App Start #######################
app = Flask(__name__)

import setting
app.config.from_object(setting)

# debug tool
toolbar = DebugToolbarExtension(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from forms import TestForm
@app.route("/test")
def test():
    form = TestForm()
    return render_template("test.html", form = form)

@app.route("/jquery")
def jquery():
    return render_template("jquery.html")

@app.route("/ajax")
def test_json():
    return jsonify(success=True)

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("image/favicon.ico")

# add modules

from view import login
from view import admin
from view import general
from view import todo
from view import photo

app.register_module(login.mod)
app.register_module(admin.mod)
app.register_module(general.mod)
app.register_module(todo.mod, url_prefix='/todo')
app.register_module(photo.mod, url_prefix='/photo')
