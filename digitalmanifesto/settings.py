"""
Django settings for digitalmanifesto project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os

import django.contrib.messages

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

# HTTPS settings
# CSRF_COOKIE_SECURE = True
#
# SESSION_COOKIE_SECURE = True

ALLOWED_HOSTS = [
    '.herokuapp.com',
    '.digitalmanifesto.net',
]

ADMINS = [
    'gwhigs@gmail.com'
]


# Application definition

INSTALLED_APPS = (
    # Core apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Project apps
    'manifestos',
    # 3rd party packages
    'grappelli',
    'django.contrib.admin',
    'autocomplete_light',
    'taggit',
    'crispy_forms',
    'floppyforms',
    'simple_history',
    'storages',
    'sorl.thumbnail',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
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
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

# Custom settings below

# One update needed for django.contrib.messages to play well with Bootstrap 3
MESSAGE_TAGS = {
    django.contrib.messages.constants.ERROR: 'danger'
}

# Grappelli customization
GRAPPELLI_ADMIN_TITLE = 'Digital Manifesto Archive'

# Crispy-forms customization
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Storages (s3 functionality)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'manifestos.custom_storages.StaticS3BotoStorage'
# DEFAULT_FILE_STORAGE = 'manifestos.custom_storages.MediaS3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# API settings

OMEKA_ENDPOINT = 'http://digitalmanifesto.omeka.net/api'

OMEKA_API_KEY = os.environ.get('OMEKA_API_KEY')

# Include local settings, if they exists
try:
    from .local_settings import *
except ImportError:
    pass