from .settings_common import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}
