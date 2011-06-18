from google.appengine.ext.webapp.util import run_wsgi_app
import ims

run_wsgi_app(ims.app)