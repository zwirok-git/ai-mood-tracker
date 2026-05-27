import os

from .base import *


DEBUG = False


DATABASES = {
    "default": {
        "ENGINE": (
            "django.db.backends.postgresql"
        ),

        "NAME": os.environ[
            "PGDATABASE"
        ],

        "USER": os.environ[
            "PGUSER"
        ],

        "PASSWORD": os.environ[
            "PGPASSWORD"
        ],

        "HOST": os.environ[
            "PGHOST"
        ],

        "PORT": os.environ.get(
            "PGPORT",
            5432,
        ),

        "OPTIONS": {
            "sslmode": "require",
        },

        "DISABLE_SERVER_SIDE_CURSORS": True,

        "CONN_HEALTH_CHECKS": True,
    },
}


EMAIL_BACKEND = (
    "anymail.backends.resend.EmailBackend"
)

DEFAULT_FROM_EMAIL = (
    "AI Mood Tracker <noreply@aimoodtracker.com>"
)

ANYMAIL = {
    "RESEND_API_KEY": os.environ[
        "RESEND_API_KEY"
    ],
}