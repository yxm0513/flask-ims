from flask import Module, render_template

mod = Module(__name__)

# URL
@mod.route('/')
def index():
    return render_template('index.html')
