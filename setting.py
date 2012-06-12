import os
# configuration

PROJ = os.path.abspath(os.path.dirname(__file__))
 
UPLOAD_FOLDER = PROJ + r'uploads'
DEBUG = True
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
DEBUG_TB_INTERCEPT_REDIRECTS = False 
DB = r'/ims/db/ims.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJ + DB
ADMIN = ['Simon', 'simon.yang.sh@gmail.com']
CSRF_ENABLED = False
UPLOADS_DEFAULT_DEST = PROJ + '/ims/uploads'
#UPLOADS_DEFAULT_URL = 'http://localhost:5000'


# default settings
DEFAULT_THEME = 'default'