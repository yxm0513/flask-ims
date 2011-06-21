# configuration

PROJ = r'/home/xinming/flask-ims'
UPLOAD_FOLDER = PROJ + r'uploads'
DEBUG = True
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
DEBUG_TB_INTERCEPT_REDIRECTS = False 
DB = r'/ims/db/ims.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJ + DB
