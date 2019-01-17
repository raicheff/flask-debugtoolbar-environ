#
# Flask-DebugToolbar-Environ
#
# Copyright (C) 2019 Boris Raicheff
# All rights reserved
#


import os

from flask_debugtoolbar.panels import DebugPanel
from jinja2 import Environment, FileSystemLoader


class EnvironPanel(DebugPanel):
    """"""

    name = 'Environ'

    has_content = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jinja_env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

    def nav_title(self):
        return self.name

    def title(self):
        return self.name

    def url(self):
        return ''

    def content(self):
        return self.render('environ.html', {'environ': os.environ})


# EOF
