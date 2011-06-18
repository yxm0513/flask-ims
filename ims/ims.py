from flask import *

import os
import setting
import models
from functools import wraps

from google.appengine.api import users

#def login_required(f):
#    @wraps(f)
#    def decorated_function(*args, **kwargs):
#        if session['username']:
#            return redirect(url_for('login', next=request.url))
#        return f(*args, **kwargs)
#    return decorated_function

###################### App Start #######################
app = Flask(__name__)
app.config.from_object(setting)

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("image/favicon.ico")

@app.route("/", methods = ['get', 'post'])
#@login_required
def index():
    user = users.get_current_user()
    if user:
        g.user = user
        g.logout_url = users.create_logout_url("/")
    else:
        g.login_url = users.create_login_url("/")
    return render_template("index.html")

@app.route('/upload', methods = ['get', 'post'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save( os.path.join(app.config['UPLOAD_FOLDER'], f.filename ))
        app.logger.debug(f.filename)
        return render_template("upload.html", msg = f.filename + " upload done")
    return render_template("upload.html", msg = '')

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)

@app.route('/downloads/')
def show_downloads():
    for root, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        return render_template('download.html', files = files)


@app.route("/test", methods = ['get', 'post'])
def test():
    user = users.get_current_user()
    if user:
        greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
                    (user.nickname(), users.create_logout_url("/")))
    else:
        greeting = ("<a href=\"%s\">Sign in or register</a>." %
                    users.create_login_url("/"))

    return greeting


if __name__ == '__main__':
    app.run(debug = True)


