import os, sys
import setting
from functools import wraps

from flask import Flask, render_template
from flaskext.debugtoolbar import DebugToolbarExtension
from flaskext.silk import Silk
from flaskext.themes import setup_themes, packaged_themes_loader

###################### App Start #######################
app = Flask(__name__)

app.config.from_object(setting)

# debug tool
toolbar = DebugToolbarExtension(app)

# themes
#packaged_themes_loader(app)
setup_themes(app, app_identifier='flask-ims')

# slik
silk = Silk(app)

# add modules
from view import test 
from view import account 
from view import admin
from view import general
from view import todo
from view import photo
from view import wiki 
from view import feed

app.register_module(test.mod)
app.register_module(account.mod)
app.register_module(admin.mod)
app.register_module(general.mod)
app.register_module(todo.mod, url_prefix='/todo')
app.register_module(photo.mod, url_prefix='/photo')
app.register_module(wiki.mod, url_prefix='/wiki')
app.register_module(feed.mod, url_prefix='/rss')
