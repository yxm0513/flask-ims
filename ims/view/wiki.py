from flask import Module, render_template
from flaskext.login import login_required
from flaskext.markdown import Markdown

mod = Module(__name__)

from ims import app
Markdown(app)

# URL
@mod.route('/')
@mod.route('/<name>', methods= ['GET'])
def show(name='MainPage'):
    # get it from database
    
    
    # render to template
    return render_template("wiki/show.html", name=name)


@mod.route('/edit_<name>', methods= ['GET', 'POST'])
# user must be logged in to edit
@login_required
def edit(name):
    if not name:
        flash()
    return render_template("wiki/edit.html", page = page, mod = "")
