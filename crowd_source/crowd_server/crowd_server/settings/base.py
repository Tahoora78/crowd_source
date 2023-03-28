
from pathlib import Path
import dj_database_url
import crowd_server
import os
from decouple import Csv, config

BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config("SECRET_KEY", default="django-insecure$crowd_server.settings.local")

DEBUG = config("DEBUG", default=True, cast=bool)

#ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "knox",
    "corsheaders",
    "rest_framework",
    "rest_framework_swagger",
    "crowd_server.apps.user",
    "crowd_server.apps.core",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



ROOT_URLCONF = "crowd_server.urls"

INTERNAL_IPS = ["127.0.0.1"]

WSGI_APPLICATION = "crowd_server.wsgi.application"


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]


if DEBUG is False:
    del MIDDLEWARE[0]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],

            'libraries' : {'staticfiles': 'django.templatetags.static'}
        },
    },
]


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

# DATABASES = {
#     "default": dj_database_url.config(
#         default=config("DATABASE_URL", default="postgres://crowd_server:crowd_server@localhost:5432/crowd_server"),
#         conn_max_age=600,
#     )
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

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


# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================

LANGUAGE_CODE = config("LANGUAGE_CODE", default="en-us")

TIME_ZONE = config("TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [BASE_DIR / "locale"]


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_URL = "/static/"

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = BASE_DIR.parent.parent / "static"


STATICFILES_DIRS = [BASE_DIR / "static"]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR.parent.parent / "media"



# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================
REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
                   'DEFAULT_PARSER_CLASSES': [
                       'rest_framework.parsers.FormParser',
                       'rest_framework.parsers.MultiPartParser',
                       'rest_framework.parsers.JSONParser',
                    ],
                    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
}


# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

CROWD_SERVER_ENVIRONMENT = config("CROWD_SERVER_ENVIRONMENT", default="local")
