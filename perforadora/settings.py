"""
Django settings for perforadora project.

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
SECRET_KEY = '%)t9^wu=1=1v)=yrkyz82bhe+w9irua3i_$n*@_9)8ibtbvi2e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'perforadora',
    'rest_framework',
    'app_planillas',
)

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'perforadora.urls'

WSGI_APPLICATION = 'perforadora.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'perforadora',
        'USER': 'root',
        'PASSWORD': 'allen',
        'HOST' : 'localhost',
        'PORT': '3306'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:7]+['static'])

#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
#STATICFILES_STORAGE = 'require.storage.OptimizedCachedStaticFilesStorage'

STATIC_URL = '/static/'

#RequireJS
#REQUIRE_BASE_URL = "app/js"


# Templates

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    os.path.abspath( os.path.join( BASE_DIR, os.pardir, 'app_planillas/templates' ) ),
)
