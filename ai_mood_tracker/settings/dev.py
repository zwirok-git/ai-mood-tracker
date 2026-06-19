from .base import *

DEBUG = True


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": ("django.contrib.staticfiles.storage.StaticFilesStorage"),
    },
}


DATABASES = {
    "default": {
        "ENGINE": ("django.db.backends.sqlite3"),
        "NAME": (BASE_DIR / "db.sqlite3"),
    },
}


ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]
