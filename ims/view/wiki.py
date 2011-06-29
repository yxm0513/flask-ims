from flask import Module, render_template
from flaskext.login import login_required
from flaskext.markdown import Markdown
from ims.forms import WikiShowForm, WikiEditForm


mod = Module(__name__)

from ims import app
Markdown(app)

# URL
@mod.route('/')
@mod.route('/<name>', methods= ['GET'])
def show(name='MainPage'):
    form = WikiShowForm()
    # get it from database
    
    
    # render to template
    return render_template("wiki/show.html", name=name, form=form)


@mod.route('/edit/<name>', methods= ['GET', 'POST'])
# user must be logged in to edit
@login_required
def edit(name):
    form = WikiEditForm()
    if not name:
        flash()
    return render_template("wiki/edit.html", form=form, name = name, mod = "")


@mod.route('/attach', methods= ['GET', 'POST'])
# user must be logged in to edit
@login_required
def attach():
    return render_template("wiki/attach.html", form=form, name = name, mod = "")


