from flask import Module, request, flash, \
    redirect, url_for
from flaskext.login import login_required
from flaskext.markdown import Markdown
from ims.models import Wiki
from ims.forms import WikiShowForm, WikiEditForm
from ims.theme import render_template

mod = Module(__name__)

from ims import app
Markdown(app)

# URL
@mod.route('/')
@mod.route('/<name>', methods= ['GET', 'POST'])
def wiki(name='MainPage'):
    if request.method == 'POST':
    #save
        if 'save' in request.form:
            wiki = Wiki.query.filter_by(title=name).first()
            form = WikiEditForm()
            if wiki:
                wiki.text = form.wikitext.data
                wiki.store_to_db()
            else: 
                wiki = Wiki(title=name, text=form.wikitext.data)
                try:
                    wiki.store_to_db()
                except:
                    app.logger.debug('failed')
            return redirect(url_for('wiki', name=name))
    #edit
        if 'edit' in request.form:
            wiki = Wiki.query.filter_by(title=name).first()
            if not wiki:
                flash("Creat a new page")
                form = WikiEditForm()
                form.set_default_text(text="Input text here")
                return render_template("wiki/edit.html", form=form, name = name)
            else:
                text = wiki.text
                form = WikiEditForm()
                form.set_default_text(text=text)
                return render_template("wiki/edit.html", form=form, name = name)
        if 'attach' in request.form:
            return render_template("wiki/attach.html", form=form, name = name)
        else:
            form = WikiShowForm()
            # get it from database
            wiki = Wiki.query.filter_by(title=name).first()
            # render to template
            return render_template("wiki/show.html", form=form, wiki=wiki, name=name)
    else:
        form = WikiShowForm()
        # get it from database
        wiki = Wiki.query.filter_by(title=name).first()
        # render to template
        return render_template("wiki/show.html", form=form, wiki=wiki, name=name)


@mod.route('/list')
def list():
    pass

@mod.route('/delete')
def delete():
    pass
