from flask import Module, render_template, request, flash
from flaskext.login import login_required
from flaskext.markdown import Markdown
from ims.models import Wiki
from ims.forms import WikiShowForm, WikiEditForm


mod = Module(__name__)

from ims import app
Markdown(app)

# URL
@mod.route('/')
@mod.route('/<name>', methods= ['GET', 'POST'])
def wiki(name='MainPage'):
    if request.method == 'POST':
    #save
        form = WikiEditForm()
        wiki = Wiki(title=name, text=form.wikitext.data)
        try:
            wiki.store_to_db
        except:
            app.logger.debug(failed)
        return render_template("wiki/show.html", form=form, name=name, wiki = wiki)
    else:
    # show and edit
        try:
            action = request.args.get('action')
        except NameError:
            action = 'show' 

        if action == 'edit':
            wiki = Wiki.query.filter_by(title=name).first()
            if not wiki:
                flash("Creat a new page")
                WikiEditForm.set_default_text(text="Input text here")
                form = WikiEditForm()
                return render_template("wiki/edit.html", form=form, name = name)
            else:
                text = wiki.text
                WikiEditForm.set_default_text(text=text)
                form = WikiEditForm()
                return render_template("wiki/edit.html", form=form, name = name, text = text)
        elif action == 'attach':
            return render_template("wiki/attach.html", form=form, name = name)
        else:
            form = WikiShowForm()
            # get it from database
            wiki = Wiki.query.filter_by(title=name).first()
               # render to template
            return render_template("wiki/show.html", form=form, wiki=wiki, name=name)


@mod.route('/list')
def list():
    pass
