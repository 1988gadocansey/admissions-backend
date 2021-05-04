"""
Django settings for management_sys project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jh$ub2&&$^w5t4c%b!_la1*24b6*=$2-4$r_k0%-js-n@4%!wv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['45.33.4.164', '127.0.0.1', 'localhost', 'ttuportal.com','https://ttuportal.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'admissions',
    'account',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
    'django.contrib.sites',
]
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
    "account.middleware.LocaleMiddleware",
    "account.middleware.TimezoneMiddleware",
]

ROOT_URLCONF = 'management_sys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates'),
            os.path.join(SITE_ROOT, 'static'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.csrf',
                "account.context_processors.account",


            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'management_sys.wsgi.application'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'admissions',
        'USER': 'gadocansey',
        'PASSWORD': '1988Gadocansey',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'Africa/Accra'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

EFAULT_FROM_EMAIL = 'noreply@ttu.edu.gh'
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_PASSWORD_EXPIRY = 60 * 60 * 24 * 5  # seconds until pw expires, this example shows five days
ACCOUNT_PASSWORD_USE_HISTORY = True
ACCOUNT_LOGIN_URL = '/login'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tpconnect@tpoly.edu.gh'
EMAIL_HOST_PASSWORD = 'ocansey2018'
EMAIL_PORT = 587
# DEFAULT_EMAIL_FROM = 'admin@payitgh.com'
ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window; you may, of course, use a different value.
ACCOUNT_OPEN_SIGNUP = True

# Pull slug max_length out ot
SLUG_MAX_LENGTH = 64

LOGIN_REDIRECT_URL = '/arms/dashboard'
LOGOUT_REDIRECT_URL = '/registration/logout'

SESSION_COOKIE_NAME = 'tpconnect'
SESSION_COOKIE_AGE = 7200  # on hour in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE =True

MESSAGE_TAGS = {
    messages.DEBUG: 'uk-alert-info',
    messages.INFO: 'uk-alert-info',
    messages.SUCCESS: 'uk-alert-success',
    messages.WARNING: 'uk-alert-warning',
    messages.ERROR: 'uk-alert-danger',
}



PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 100,
    'MARGIN_PAGES_DISPLAYED': 2,

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

ADMINS = [('Gad Ocansey', 'gadocansey@gmail.com')]



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = []
# Statici18n Config
STATICI18N_ROOT = os.path.join(SITE_ROOT, 'static')

STATICFILES_DIRS += [STATICI18N_ROOT]

STATIC_ROOT = os.path.join(SITE_ROOT, 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

