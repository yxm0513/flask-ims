from datetime import datetime
from flaskext.sqlalchemy import SQLAlchemy

from ims import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, )
    password = db.Column(db.String(80))
    email = db.Column(db.String(120))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column('todo_id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.String)
    done = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()

class Photo(db.Model):
    id = db.Column('todo_id', db.Integer, primary_key=True)
    filename = db.Column(db.String(60))
    user = db.Column(db.Integer)
    
    def __init__(self, filename, user):
        self.filename = filename
        self.user = user

    def store(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def load(cls, id):
        photo = cls.query.filter_by(user = id).first()
        return photo
            
        
