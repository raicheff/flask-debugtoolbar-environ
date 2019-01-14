#
# Flask-DebugToolbar-More
#
# Copyright (C) 2019 Boris Raicheff
# All rights reserved
#


import os

from flask_debugtoolbar.panels import DebugPanel
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader


_ = lambda x: x


class EnvironDebugPanel(DebugPanel):
    """"""

    name = 'Environ'

    has_content = True

    def __init__(self, jinja_env, **kwargs):
        super().__init__(jinja_env, **kwargs)
        jinja_env.loader = ChoiceLoader([
            jinja_env.loader,
            PrefixLoader({
                'flask-debugtoolbar-more': PackageLoader(__name__, 'templates')
            })
        ])

    def nav_title(self):
        return _('Environment')

    def title(self):
        return _('Environment')

    def url(self):
        return ''

    def content(self):
        context = self.context.copy()
        context.update({'environ': os.environ})
        return self.render('flask-debugtoolbar-more/environ.html', context)


# EOF
