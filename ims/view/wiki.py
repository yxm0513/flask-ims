from flask import Module, render_template, request
from flaskext.login import login_required
from flaskext.markdown import Markdown
from ims.forms import WikiShowForm, WikiEditForm


mod = Module(__name__)

from ims import app
Markdown(app)

# URL
@mod.route('/')
@mod.route('/<name>', methods= ['GET'])
def wiki(name='MainPage'):
    try:
        action = request.args.get('action')
    except NameError:
        action = 'show' 

    if action == 'edit':
        form = WikiEditForm()
        if not name:
            flash("Creat a new page")
        return render_template("wiki/edit.html", form=form, name = name, mod = "")
    elif action == 'attach':
        return render_template("wiki/attach.html", form=form, name = name, mod = "")
    else:
        form = WikiShowForm()
        # get it from database
    
    
           # render to template
        return render_template("wiki/show.html", name=name, form=form)
