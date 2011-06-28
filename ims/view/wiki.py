from flask import Module, render_template

mod = Module(__name__)

# URL
@mod.route('/wiki/<name>', methods= ['GET'])
def show(name):
    if not name:
        name = 'MainPage'
    
    # get it from database
    
    
    # render to template
    return render_template("wiki/show.html", page = page, mod = "")


@mod.route('/wiki/edit_<name>', methods= ['GET', 'POST'])
''' user must be logged in to edit '''
@login_required
def edit(name):
    if not name:
        flash()
    return render_template("wiki/edit.html", page = page, mod = "")
