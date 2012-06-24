from flask import Module
from ims.theme import render_template
#from xhtml2pdf import pisa
#from cStringIO import StringIO




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

@mod.route('/about')
def about():
    return render_template("general/about.html")

@mod.route('/')
def index():
    return render_template('general/index.html')

#@mod.route('/pdf')
#def pdf(pdf_data):
#    pdf = StringIO()
#    pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
#    return pdf

