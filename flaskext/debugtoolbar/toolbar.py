from flask import url_for, current_app

class DebugToolbar(object):
    def __init__(self, request, jinja_env):
        self.jinja_env = jinja_env
        self.request = request
        self.panels = []

        # default config settings
        self.config = {
            'DEBUG_TB_INTERCEPT_REDIRECTS': True,
            'DEBUG_TB_PANELS': (
                'flaskext.debugtoolbar.panels.versions.VersionDebugPanel',
                'flaskext.debugtoolbar.panels.timer.TimerDebugPanel',
                'flaskext.debugtoolbar.panels.headers.HeaderDebugPanel',
                'flaskext.debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
                'flaskext.debugtoolbar.panels.template.TemplateDebugPanel',
                'flaskext.debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
                'flaskext.debugtoolbar.panels.logger.LoggingPanel',
                'flaskext.debugtoolbar.panels.profiler.ProfilerDebugPanel',

            )
        }
        self.config.update(current_app.config)

        self.template_context = {
            'static_path': url_for('_debug_toolbar.static', filename='')
        }

        self.default_panels = self.config['DEBUG_TB_PANELS']
        self.load_panels()


    def load_panels(self):
        """
        Populate debug panels
        """
        activated = self.request.cookies.get('fldt_active', '').split(';')
        for panel_path in self.default_panels:
            dot = panel_path.rindex('.')
            panel_module, panel_classname = panel_path[:dot], panel_path[dot+1:]

            mod = __import__(panel_module, {}, {}, [''])
            panel_class = getattr(mod, panel_classname)

            panel_instance = panel_class(
                context=self.template_context,
                jinja_env=self.jinja_env)

            if panel_instance.dom_id() in activated:
                panel_instance.is_active = True
            self.panels.append(panel_instance)

    def render_toolbar(self):
        context = self.template_context.copy()
        context.update({'panels': self.panels})

        template = self.jinja_env.get_template('base.html')
        return template.render(**context)


