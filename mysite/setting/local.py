# Import the base settings
from .base import *

# Override settings for local development
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
# Other local-specific settings can be added here
SITE_ID = 3
SECRET_KEY = 'django-insecure-3j%qj46=3+-rccf#6a3%(xq0#q^qk*fr8_c%qn-xnx+rutk%0y'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'

# Media files configuration
MEDIA_ROOT = BASE_DIR / 'media'

# Additional static files directories
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS = "SAMEORIGIN"


