from flask import current_app, session
from flaskext.themes import render_theme_template

def render_template(template, **context):
    theme = session.get('theme', current_app.config['DEFAULT_THEME'])
    return render_theme_template(theme, template, **context)
