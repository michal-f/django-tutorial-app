import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
SECRET_KEY = '!)f-qg)65)ij()&zq0+(fn(r9f6r+p@$jrxi#)s^h%(ibmw5h*'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = ('django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'jquery',
                  'polls',
                  'django_countries')

LOGIN_URL = '/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [os.path.join(BASE_DIR, 'templates')],
              'APP_DIRS': True,
              'OPTIONS': {'context_processors': ['django.template.context_processors.debug',
                                                 'django.template.context_processors.request',
                                                 'django.contrib.auth.context_processors.auth',
                                                 'django.contrib.messages.context_processors.messages']}}]

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3',
                         'NAME': os.path.join(BASE_DIR, 'db.sqlite3')}}

LANGUAGE_CODE = 'en-us'


from django.utils.translation import ugettext_lazy as _

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
    ('pl', _('Polish')),
]
LOCALE_PATHS = (
    os.path.join(ROOT_DIR, 'locale'),
)


TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True
DATETIME_FORMAT = 'H:i:s - d M Y'

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(ROOT_DIR),
                    os.path.join(ROOT_DIR, "static"))

STATIC_ROOT = os.path.join(ROOT_DIR, 'public', 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, 'public', 'media/')

FIXTURE_DIRS = [os.path.join(ROOT_DIR, "fixtures")]