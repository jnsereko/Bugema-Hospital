INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    # ...
]
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
DEBUG = False
MIDDLEWARE = [
   # This is the default Django Security Middleware
   'django.middleware.security.SecurityMiddleware',
   
   # Add whitenoise middleware here
   'whitenoise.middleware.WhiteNoiseMiddleware',
   # ...
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)