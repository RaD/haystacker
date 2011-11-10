# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

import os, sys

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

gettext_noop = lambda s: s

# Django settings for haystacker project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ruslan Popov', 'ruslan.popov@gmail.com'),
)

MANAGERS = ADMINS

AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = '<project_name>'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'haystacker',
        'USER': 'haystacker',
        'PASSWORD': 'q1',
        'HOST': 'localhost',
        'PORT': '',
    }
}

FIRST_DAY_OF_WEEK = 1

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru'
LANGUAGES = (
          ('en', gettext_noop('English')),
          ('ru', gettext_noop('Russian')),
    )

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = rel('media')
MEDIA_URL = '/media/'
STATIC_ROOT = rel('static_root')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_DIRS = DEBUG and (rel('static'),) or None
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = '123'
SESSION_COOKIE_NAME = 'haystacker_sessionid'

if DEBUG:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
else:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    #'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'context_templates.common_vars',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

FIXTURE_DIRS = ( rel('fixtures'), )

TEMPLATE_DIRS = ( rel('templates'), )

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

INSTALLED_APPS = (
    # base
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.admindocs',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',

    # applications
    'text',
)

###
# haystack
###

INSTALLED_APPS += ('haystack',)
HAYSTACK_SEARCH_ENGINE = 'xapian' # xapian, whoosh
HAYSTACK_SITECONF = 'haystack_init'
HAYSTACK_XAPIAN_PATH = rel('xapian_index')
HAYSTACK_WHOOSH_PATH = rel('whoosh_index')

###
# Logger
###

LOGGING_DIR = '/home/django/logs'

###
# Emergency settings for production
# Please avoid this way if possible
###

try:
    from settings_local import *
except ImportError:
    pass
