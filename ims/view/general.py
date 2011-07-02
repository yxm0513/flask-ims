from flask import Module, render_template

mod = Module(__name__)

@mod.route("/favicon.ico")
def favicon():
    return mod.send_static_file("image/favicon.ico")

# URL
@mod.route('/settings')
def settings():
    return render_template("general/settings.html")

@mod.route('/help')
def help():
    return render_template("general/help.html")

@mod.route('/')
def index():
    return render_template('general/index.html')


