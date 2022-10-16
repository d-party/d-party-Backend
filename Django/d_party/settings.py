"""
Django settings for d_party project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import socket

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ["DEBUG"] == "1"

ALLOWED_HOSTS = [os.environ["MY_DOMAIN"], "www." + os.environ["MY_DOMAIN"]]
if DEBUG:
    ALLOWED_HOSTS += ["*"]
CSRF_TRUSTED_ORIGINS = [
    "https://*." + os.environ["MY_DOMAIN"],
    "https://*.127.0.0.1",
    "wss://*." + os.environ["MY_DOMAIN"],
    "wss://*.127.0.0.1",
]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_crontab",
    "django_extensions",
    "channels",
    "debug_toolbar",
    "django_boost",
    "rest_framework",
    "axes",
    "request",
    "django_prometheus",
    "streamer",
    "web",
    "api",
]

AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
]

MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "request.middleware.RequestMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "axes.middleware.AxesMiddleware",
    "debreach.middleware.RandomCommentMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]
if DEBUG:
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

ROOT_URLCONF = "d_party.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "d_party.wsgi.application"

# redis
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {"hosts": [("redis", 6379)]},
    }
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ["DATABASE_ENGINE"],
        "NAME": os.environ["MYSQL_DATABASE"],
        "USER": os.environ["DATABASE_USER"],
        "PASSWORD": os.environ["MYSQL_ROOT_PASSWORD"],
        "HOST": os.environ["DATABASE_HOST"],
        "PORT": os.environ["DATABASE_PORT"],
        "TEST": {
            "NAME": "test_db",
            "MIRROR": "default",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = os.environ["LANGUAGE_CODE"]

TIME_ZONE = os.environ["TIME_ZONE"]

USE_I18N = True

USE_TZ = True

JAZZMIN_SETTINGS = {
    "site_title": "d-party",
    "site_header": "d-party",
    "site_brand": "d-party",
    "site_logo": "web/logo/dp-mini.png",
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome to d-party",
    "copyright": "d-party",
    "search_model": "auth.User",
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {
            "name": "Support",
            "url": "https://github.com/farridav/django-jazzmin/issues",
            "new_window": True,
        },
        {
            "name": "Develop",
            "url": "https://github.com/d-Party",
            "new_window": True,
        },
        {
            "name": "Chart",
            "url": "/admin/chart",
            "new_window": True,
        },
        {
            "name": "grafana",
            "url": "/grafana/",
            "new_window": True,
        },
        {"model": "auth.User"},
        {"model": "streamer.AnimeRoom"},
        {"model": "streamer.TVRoom"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {
            "name": "Support",
            "url": "https://github.com/farridav/django-jazzmin/issues",
            "new_window": True,
        },
        {"model": "auth.user"},
    ],
    #############
    # Side Menu #
    #############
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    "custom_links": {
        "books": [
            {
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["books.view_book"],
            }
        ]
    },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Channels
ASGI_APPLICATION = "d_party.asgi.application"

# axes
AXES_FAILURE_LIMIT = 10
AXES_COOLOFF_TIME = 6
AXES_ONLY_USER_FAILURES = True
AXES_RESET_ON_SUCCESS = True

if DEBUG:
    AXES_ENABLED = False

# django-extensions
RUNSERVERPLUS_SERVER_ADDRESS_PORT = "0.0.0.0:8000"

# django-crontab

if DEBUG:
    CRON_SCHEDULE = "* * * * *"
else:
    CRON_SCHEDULE = "0 0 * * *"

CRONJOBS = [
    (
        CRON_SCHEDULE,
        "streamer.cron.animeroom_auto_logical_delete",
        ">> /var/log/cron.log",
    ),
    (
        CRON_SCHEDULE,
        "streamer.cron.animeuser_auto_logical_delete",
        ">> /var/log/cron.log",
    ),
    (
        CRON_SCHEDULE,
        "streamer.cron.animeroom_auto_hard_delete",
        ">> /var/log/cron.log",
    ),
    (
        CRON_SCHEDULE,
        "streamer.cron.animeuser_auto_hard_delete",
        ">> /var/log/cron.log",
    ),
    (
        CRON_SCHEDULE,
        "streamer.cron.animereaction_auto_hard_delete",
        ">> /var/log/cron.log",
    ),
]
if DEBUG:
    CRONTAB_COMMAND_SUFFIX = "2>&1"

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}
