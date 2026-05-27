import os

from .base import *


DEBUG = False

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECRET_KEY = os.environ["SECRET_KEY"]

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
   ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)



DATABASES = {
    "default": {
        "ENGINE": (
            "django.db.backends.postgresql"
        ),
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ["POSTGRES_DB_PORT"],
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}


EMAIL_BACKEND = (
    "anymail.backends.resend.EmailBackend"
)

DEFAULT_FROM_EMAIL = (
    "AI Mood Tracker <noreply@ai-mood-tracker.site>"
)

ANYMAIL = {
    "RESEND_API_KEY": os.environ[
        "RESEND_API_KEY"
    ],
}

