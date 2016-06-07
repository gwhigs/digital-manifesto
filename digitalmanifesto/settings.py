"""
Django settings for digitalmanifesto project.

The following additional values must be set, either in a local_settings.py
(development) or with environment variables (production):
    SECRET_KEY
    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME
    DATABASE_URL
    DB_HOST
    DB_NAME
    DB_PASSWORD
    DB_PORT
    DB_USER
    OMEKA_API_KEY

In addition, the following Heroku addons (along with their default env vars)
are required in production:
    SendGrid
    Soon:
        Heroku Redis:
            heroku addons:create heroku-redis:free --timeout 60 --maxmemory volatile-lru

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os

import django.contrib.messages

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

TEMPLATE_DEBUG = False

# SSL Settings (always force https in production)
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Heroku setting for SSL redirection (avoids redirect loop)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = [
    '.herokuapp.com',
    '.digitalmanifesto.net',
    '127.0.0.1',
]

ADMINS = [
    ('Graham Higgins', 'gwhigs@gmail.com'),
]

# CREDIT TO https://github.com/jordn/heroku-django-s3/
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Sendgrid settings
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definitions

INSTALLED_APPS = (
    # Core apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Admin
    # 'jet',
    'django.contrib.admin',
    # Project apps
    'manifestos',
    'annotations',
    # 3rd party packages
    'dal',
    'dal_select2',
    'taggit',
    'crispy_forms',
    'floppyforms',
    'simple_history',
    'storages',
    'sorl.thumbnail',
    'analytical',
    'rest_framework',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # corsheaders plugin should be listed befor django's CommonMiddleware
    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Simple History pkg functionality
    'simple_history.middleware.HistoryRequestMiddleware',
)

ROOT_URLCONF = 'digitalmanifesto.urls'

WSGI_APPLICATION = 'digitalmanifesto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
    }
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Django defaults
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.static",
                "django.core.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                # Extra Core: add the current HttpRequest to RequestContext
                "django.template.context_processors.request",
            ]
        }
    }
]

# Custom settings below

# One update needed for django.contrib.messages to play well with Bootstrap 3
MESSAGE_TAGS = {
    django.contrib.messages.constants.ERROR: 'danger'
}

# Crispy-forms customization
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Storages (s3 functionality)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'manifestos.custom_storages.StaticS3BotoStorage'
# DEFAULT_FILE_STORAGE = 'manifestos.custom_storages.MediaS3BotoStorage'

AWS_QUERYSTRING_AUTH = False

# === SECRETS ===

# AWS
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# Twitter
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_KEY = os.environ.get('TWITTER_ACCESS_KEY')
TWITTER_ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET')


# Enable django-analytical services
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-51926542-1'

# django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True
CORS_EXPOSE_HEADERS = (
    'Access-Control-Allow-Origin: *',
)


# API settings

OMEKA_ENDPOINT = 'http://digitalmanifesto.omeka.net/api'
OMEKA_API_KEY = os.environ.get('OMEKA_API_KEY')

# Custom app settings
ANNOTATION_TEXT_OBJECT = 'manifestos.Manifesto'

# Include local settings, if they exists
try:
    from .local_settings import *
except ImportError:
    pass
