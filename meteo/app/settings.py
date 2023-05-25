import os
from os.path import dirname
from django.utils.translation import gettext_lazy as _

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "meteo").split(",")
CSRF_TRUSTED_ORIGINS = os.environ.get("DOMAIN_URL", "http://localhost:8000").split(",")

BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, "content")

SECRET_KEY = os.environ.get(
    "SECRET_KEY", "SkcNkSnCs3nU3a4Fi9hXxmNTn3n5UuyeuM5CwNT8oVyERdC4cXf4ahYem3SEJ7Tg"
)

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Vendor apps
    "bootstrap4",
    # Application apps
    "main",
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "accounts.middleware.UserCookieMiddleWare",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(CONTENT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USERNAME"),
        "PASSWORD": os.environ.get("DB_PASSWD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": "3306",
        "OPTIONS": {
            "read_default_file": "/etc/mysql/my.cnf",
            "charset": "utf8mb4",
            "use_unicode": True,
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGIN_REDIRECT_URL = "index"
LOGIN_URL = "accounts:log_in"

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

TIME_ZONE = "UTC"
USE_TZ = True

STATIC_ROOT = "/static"
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, "assets"),
]

SIGN_UP_FIELDS = ["username", "password1", "password2"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

FLAG = "lh2023{5pXQCuV4EjvZA7JAyYWs6CUrF2R8aL9G}"
