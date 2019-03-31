from tutoriel_django.settings import *

import dj_database_url

DEBUG = False

TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = 'ocx4+waga8*@3&=r^=c0php+8^#y4y6%ik6xv_l&dzii*mr^n_'

ALLOWED_HOSTS = [
'easy-blog-django.herokuapp.com', 
]

