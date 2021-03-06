# -*- coding: utf-8 -*-
"""
Django settings for test_django_admin_bootstrapped project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3!^@q06fn2-zl%2f%rmux58ybi9u=9k_lq^k*+^429foc#7fzn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'bootstrap3',
    'django_admin_bootstrapped',
    'filer',
    'easy_thumbnails',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'test_django_admin_bootstrapped',
    'CapitalApp',
    'TestCapital',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.template.context_processors.request',
)

ROOT_URLCONF = 'test_django_admin_bootstrapped.urls'

WSGI_APPLICATION = 'test_django_admin_bootstrapped.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django theme suit configurations
SUIT_CONFIG = {
    'MENU': (
        {'app': 'auth',
         'label': u'账号管理',
         'models': ('user', 'group')
        },
        {'app': 'auth',
         'label': u'账号管理',
         'models': ('user', 'group')
        },
        {'app': 'CapitalApp',
         'label': u'Capitalapp自定义名字',
         'models': ('capitalmodel',),
        },
        {'app': 'TestCapital',
         'label': u'Capitalapp自定义名字',
         'models': ('testcapitalmodel',),
        },
        {'label': u'帮助',
         'models': ({'label': u'商家管理',
                     'url': '/utils/userplus_help/'},
                    {'label': u'众筹系统',
                     'url': '/utils/crowdfund_help/'},
                    )
         },
         {'label': u'帮助2',
         'models': ({'label': u'商家管理',
                     'url': '/utils/userplus_help/'},
                    {'label': u'众筹系统',
                     'url': '/utils/crowdfund_help/'},
                    )
         }
     ),
}
