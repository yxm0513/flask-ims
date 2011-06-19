# configuration

PROJECT = r'.'
UPLOAD_FOLDER = PROJECT + r'uploads'
DB = PROJECT + r'/db/ims.db'
DEBUG = True
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
DEBUG_TB_INTERCEPT_REDIRECTS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB
