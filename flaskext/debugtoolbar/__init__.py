import os

from flask import current_app, request, signals
from flask.globals import _request_ctx_stack
from flask.helpers import send_from_directory
from jinja2 import Environment, PackageLoader
from werkzeug.exceptions import HTTPException

from flaskext.debugtoolbar.toolbar import DebugToolbar

def replace_insensitive(string, target, replacement):
    """
    Similar to string.replace() but is case insensitive
    Code borrowed from: http://forums.devshed.com/python-programming-11/case-insensitive-string-replace-490921.html
    """
    no_case = string.lower()
    index = no_case.rfind(target.lower())
    if index >= 0:
        return string[:index] + replacement + string[index + len(target):]
    else: # no results so return the original string
        return string


class DebugToolbarExtension(object):
    _static_dir = os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'static'))

    _redirect_codes = [301, 302, 303, 304]

    def __init__(self, app):
        self.app = app
        self.debug_toolbars = {}

        signals.request_started.connect(self.process_request, app)
        signals.request_finished.connect(self.process_response, app)

        # Monkey-patch the Flask.dispatch_request method
        app.dispatch_request = self.dispatch_request

        # Configure jinja for the internal templates and add url rules
        # for static data
        self.jinja_env = Environment(
            extensions=['jinja2.ext.i18n'],
            loader=PackageLoader(__name__, 'templates'))

        app.add_url_rule('/_debug_toolbar/static/<path:filename>',
            '_debug_toolbar.static', self.send_static_file)


    def dispatch_request(self):
        """Does the request dispatching.  Matches the URL and returns the
        return value of the view or error handler.  This does not have to
        be a response object.  In order to convert the return value to a
        proper response object, call :func:`make_response`.

        This is a modified version of the default Flask.dispatch_request
        """
        req = _request_ctx_stack.top.request
        app = current_app
        try:
            if req.routing_exception is not None:
                raise req.routing_exception
            rule = req.url_rule
            # if we provide automatic options for this URL and the
            # request came with the OPTIONS method, reply automatically
            if getattr(rule, 'provide_automatic_options', False) \
               and req.method == 'OPTIONS':
                return app.make_default_options_response()

            # otherwise dispatch to the handler for that endpoint, give the
            # panels the ability to wrap the view_func
            view_func = app.view_functions[rule.endpoint]
            view_func = self.process_view(app, view_func, req.view_args)

            return view_func(**req.view_args)

        except HTTPException, e:
            return app.handle_http_exception(e)

    def _show_toolbar(self):
        if request.path.startswith('/_debug_toolbar/'):
            return False

        return True

    def send_static_file(self, filename):
        return send_from_directory(self._static_dir, filename)

    def process_request(self, app):
        if not self._show_toolbar():
            return

        self.debug_toolbars[request] = DebugToolbar(request, self.jinja_env)
        for panel in self.debug_toolbars[request].panels:
            panel.process_request(request)

    def process_view(self, app, view_func, view_kwargs):
        if request in self.debug_toolbars:
            for panel in self.debug_toolbars[request].panels:
                new_view = panel.process_view(request, view_func, view_kwargs)
                if new_view:
                    view_func = new_view
        return view_func

    def process_response(self, sender, response):
        if request not in self.debug_toolbars:
            return response

        if self.debug_toolbars[request].config['DEBUG_TB_INTERCEPT_REDIRECTS']:
            if response.status_code in self._redirect_codes:
                redirect_to = response.location
                redirect_code = response.status_code
                if redirect_to:
                    response.location = None
                    response.status_code = 200
                    response.response = [
                        self.render('redirect.html', {
                            'redirect_to': redirect_to,
                            'redirect_code': redirect_code})]

        if response.status_code == 200:
            for panel in self.debug_toolbars[request].panels:
                panel.process_response(request, response)

            if response.is_sequence:
                response_html = response.data.decode(response.charset)
                toolbar_html = self.debug_toolbars[request].render_toolbar()
                response.response = [
                    replace_insensitive(
                        response_html,
                        '</body>',
                        toolbar_html + '</body>')]
                
    def render(self, template_name, context):
        template = self.jinja_env.get_template(template_name)
        return template.render(**context)
