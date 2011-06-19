import os, sys
import setting
from functools import wraps

from flask import Flask, render_template
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.debugtoolbar import DebugToolbarExtension


###################### App Start #######################
app = Flask(__name__)

# debug tool
toolbar = DebugToolbarExtension(app)

@app.route("/test")
def test():
    return render_template("test.html")

#@app.route("/favicon.ico")
#def favicon():
#    return app.send_static_file("image/favicon.ico")

# add modules
from view import general
app.register_module(general.mod)

    
if __name__ == '__main__':
    app.run()
