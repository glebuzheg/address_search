import os

if os.environ.get('DYNO_RAM'):
    from .settings_heroku import *
else:
    from .settings_dev import *
