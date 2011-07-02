from flask import Module, render_template, jsonify

mod = Module(__name__)

from ims.forms import TestForm
@mod.route("/test")
def test():
    form = TestForm()
    return render_template("test/test.html", form = form)

@mod.route("/jquery1")
def jquery1():
    return render_template("test/jquery_antimate.html")

@mod.route("/jquery2")
def jquery2():
    return render_template("test/jquery_slide.html")

@mod.route("/json")
def json():
    return jsonify(success=True)

