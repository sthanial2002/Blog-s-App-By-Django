from tutoriel_django.settings import *

import dj_database_url

DEBUG = True

TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = get_env_variable('SECRET_KEY')

ALLOWED_HOSTS = [
'easyblog-by-django.herokuapp.com', 
]

MIDDLEWARE += [
  'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
