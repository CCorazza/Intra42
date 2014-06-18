import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEFAULT_FROM_EMAIL = 'ccorazza@student.42.fr'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ccorazza@student.42.fr'
EMAIL_HOST_PASSWORD = 'mCKb0ss4815162342'
EMAIL_PORT = 468
EMAIL_USE_TLS = True
APPEND_SLASH = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


### ------------------------------------- Apps ---------------------------------------

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'auth',
    'forum',
    'modules',
    'tickets',
    'users',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

### ------------------------------- Templates & URLs -------------------------------

ROOT_URLCONF = 'intra.urls'

WSGI_APPLICATION = 'intra.wsgi.application'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'intra', 'templates'),
    os.path.join(BASE_DIR, 'modules', 'templates'),
)

PYBB_TEMPLATE = 'intra/base.html'

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
)

### ------------------------------- Medias && Statics -------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'intra', 'static'),
)

### ------------------------------------ Logging ------------------------------------

SECRET_KEY = '%)c%ub^d&x0n(s0+)opml4=gjyy@bu2ukcenskc#4pg#n^xa^0'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

ALLOWED_HOSTS = []

ADMINS = (
    (u'root', 'ccorazza@student.42.fr')
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'intra42',
        'USER': 'root',
        'PASSWORD': 'toor',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

### ------------------------------------ I18N ------------------------------------

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)
