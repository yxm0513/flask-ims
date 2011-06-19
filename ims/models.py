from flaskext.sqlalchemy import SQLAlchemy

from flask import current_app

db = SQLAlchemy(current_app)
class Post(db.Model):
    _tablename = 'post'
