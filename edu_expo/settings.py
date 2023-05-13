import ast
import os
from pathlib import Path
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def get_bool_from_env(name, default_value):
    if name in os.environ:
        value = os.environ[name]
        try:
            return ast.literal_eval(value)
        except ValueError as e:
            raise ValueError("{} is an invalid value for {}".format(value, name)) from e
    return default_value


def get_list(text):
    return [item.strip() for item in text.split(",")]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = get_list(os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1"))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.student',
    'apps.school',
    'apps.course',
    'crispy_forms',
    "crispy_bootstrap5",
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'edu_expo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'edu_expo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Database
db_type = os.environ.get('DB_TYPE', default='SqlLite')
if db_type == 'SqlLite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'classmateshop.db.sqlite3'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE'),
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER', " get_bool_from_env('DB_NAME',"),
            'PASSWORD': os.environ.get('DB_PASSWORD', ""),
            'HOST': os.environ.get('DB_HOST', ""),
            'PORT': os.environ.get('DB_PORT', "5432"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ.get('TIME_ZONE', 'Asia/Kolkata')

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL_CONFIGURATION
email = get_bool_from_env('EMAIL', False)
if email is True:
    EMAIL_BACKEND = 'django.project_name.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_PORT = os.environ.get('EMAIL_PORT')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = get_bool_from_env('EMAIL_USE_TLS', True)
    FROM_EMAIL = os.environ.get('FROM_EMAIL')

# development
dev_env = os.environ.get('DJ_ENV')
if dev_env == 'development':
    DEBUG = True
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    EMAIL_BACKEND = 'django.project_name.mail.backends.console.EmailBackend'
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ['127.0.0.1', 'localhost']

# CELERY CONGIGURATION
celery = get_bool_from_env('CELERY', False)
if celery is True:
    INSTALLED_APPS += ['django_celery_results', 'django_celery_beat']
    CELERY_BROKER_URL = os.environ.get('REDIS_LOCATION')
    CELERY_RESULT_BACKEND = 'django-db'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = TIME_ZONE
    CELERY_CREATE_MISSING_QUEUES = True
    CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# CACHE CONFIGURATION
cache = get_bool_from_env('CACHE', False)
if cache is True:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": os.environ.get('REDIS_LOCATION'),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }

# AMAZON S3 CONFIGURATION
do_space = get_bool_from_env('DO_SPACE', False)
if do_space is True:
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL", None)
    AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN")
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    STATICFILES_LOCATION = os.environ.get("STATICFILES_LOCATION")
    MEDIAFILES_LOCATION = os.environ.get("MEDIAFILES_LOCATION")
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
    AWS_LOCATION = os.environ.get("AWS_LOCATION", "")
    AWS_DEFAULT_ACL = os.environ.get("AWS_DEFAULT_ACL", None)
    AWS_S3_FILE_OVERWRITE = get_bool_from_env("AWS_S3_FILE_OVERWRITE", False)
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

do_cdn = get_bool_from_env('DO_CDN', False)
if do_cdn is True:
    AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN")

sentry = get_bool_from_env('SENTRY', True)
if sentry is True:
    sentry_sdk.init(dsn=os.environ.get('SENTRY_DSN'), integrations=[DjangoIntegration()])

logging = get_bool_from_env('logging', True)
if logging is True:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {"level": "INFO", "handlers": ["console"]},
        "formatters": {
            "verbose": {
                "format": (
                    "%(levelname)s %(name)s %(message)s [PID:%(process)d:%(threadName)s]"
                )
            },
            "simple": {"format": "%(levelname)s %(message)s"},
        },
        "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
        "handlers": {
            "mail_admins": {
                "level": "ERROR",
                "filters": ["require_debug_false"],
                "class": "django.utils.log.AdminEmailHandler",
            },
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console", "mail_admins"],
                "level": "INFO",
                "propagate": True,
            },
            "django.server": {"handlers": ["console"], "level": "INFO", "propagate": True},
            "app": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        },
    }

# cors settings
cors = get_bool_from_env('CORS', False)
if cors is True:
    INSTALLED_APPS += ['corsheaders']
    MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware', ]
    CORS_ORIGIN_WHITELIST = get_list(
        os.environ.get('CORS_ORIGIN_WHITELIST', 'http://localhost:3000,http://127.0.0.1:3000'))

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

CSRF_TRUSTED_ORIGINS = get_list(os.environ.get('CSRF_TRUSTED_ORIGINS', 'http://localhost:8009'))
