"""
Django settings for django_test project.

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
SECRET_KEY = os.environ['SECRET_KEY']
# SECRET_KEY = '01wn%mg_nh0mhwu_+nnhv6%na4b-2=23zbyt0_8x+k-ut((y3+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Template directories
TEMPLATE_DIRS = (
	BASE_DIR+'/templates',
	BASE_DIR+'/articles/templates',
	BASE_DIR+'/userprofile/templates',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.formtools',
	'django_test',
	'article',
	'userprofile',
	'south',
    'bootstrap_toolkit',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_test.urls'

WSGI_APPLICATION = 'django_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'data',
        'USER' : 'django',
        'PASSWORD' : 'django',
        },
    }

LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'standard': {
			'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
		}
	},
	'handlers': {
		'default': {
			'level':'DEBUG',
			'class':'logging.handlers.RotatingFileHandler',
			'filename': BASE_DIR+'/logs/mylog.log',
			'maxBytes': 1024*1024*2,   # 2MB
			'backupCount': 5,
			'formatter':'standard',
		},
		'request_handler': {
			'level':'DEBUG',
			'class':'logging.handlers.RotatingFileHandler',
			'filename': BASE_DIR+'/logs/django_request.log',
			'maxBytes': 1024*1024*2,  # 2MB
			'backupCount': 5,
			'formatter':'standard',
		},
	},
	'loggers': {
		'': {
			'handlers': ['default'],
			'level': 'DEBUG',
			'propagate': True
		},
		'django.request': {
			'handlers': ['request_handler'],
			'level': 'DEBUG',
			'propagate': False
		},
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Media files
MEDIA_ROOT = BASE_DIR+'/static'

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = ''
STATIC_URL = '/static/'

PARENT_DIR = os.path.abspath(os.path.dirname(__file__) + "/../../")

# grab email pw from parent directory (not in repo)
# this is work-around until figure out how to set env vars on EC2 instance
fname = PARENT_DIR+'/.email'
if os.path.isfile(fname):
	EMAIL_HOST_PASSWORD = open(fname, 'r').read()[:16]
else:
	EMAIL_HOST_PASSWORD = ""

# gmail SMTP setup
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ugikma@gmail.com'

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

# references:
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# http://www.lleess.com/2013/05/install-django-on-apache-server-with.html#.UweiYDddV39

