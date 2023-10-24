# Import the base settings
import secrets
from .base import *

# Override settings for production
DEBUG = False
ALLOWED_HOSTS = ['ansrza.ir','www.ansrza.ir',]
# Set database, secret key, and other production-specific settings here
SECURE_HSTS_SECONDS = 31536000  # Example: One year in seconds
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True# Import the secrets module

# Set a strong and random SECRET_KEY
SECRET_KEY = secrets.token_urlsafe(50)


