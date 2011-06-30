from flask import Module, render_template

mod = Module(__name__)

# URL
@mod.route('/settings')
def settings():
    return render_template("settings.html")

@mod.route('/help')
def help():
    return render_template("help.html")

@mod.route('/')
def index():
    return render_template('index.html')


