"""
Django settings for terms_gen_home project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from datetime import timedelta
import os
import sys
import dj_database_url
from django.core.management.utils import get_random_secret_key
# import django_heroku

import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("DEBUG", "False") == "True"
DEBUG = False
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
# DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

# Application definition
AUTH_USER_MODEL = 'users.User'
INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'p_p',
    't_c',
    'users',
    'rest_framework',
    'django.contrib.admin',
    'rest_framework_simplejwt',
    'django_rest_passwordreset',
    'drf_yasg',
    'corsheaders',
    'phonenumber_field',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'terms_gen_home.urls'
CORS_URLS_REGEX = r"^/api/.*"
# CORS_ALLOWED_ORIGINS = []
CORS_ALLOWED_ORIGINS = [
        # add allowed origins here
        'http://127.0.0.1:5500',
        'http://127.0.0.1:3000',
        'http://127.0.0.1:5500',
        'http://127.0.0.1:5501',
        'https://abshaibu.github.io',
    ]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = env('EMAIL')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# if DEBUG:

auth_classes = [
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework_simplejwt.authentication.JWTAuthentication',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': auth_classes,
    "DEFAULT_PERMISSION_CLASSES": [
        'rest_framework.permissions.AllowAny'
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ]
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'terms_gen_home.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

postgresql_DB = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nginxdb',
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
sqlite_DB = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Deployed_DB = {
#     'default': dj_database_url.config(
#         default=env('DATABASE_URL'))
# }
# if DEBUG:
DATABASES = postgresql_DB
# else:
# DATABASES = Deployed_DB

# DATABASES = sqlite_DB

# if DEVELOPMENT_MODE is True:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#         }
#     }
# elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
#     if os.getenv("DATABASE_URL", None) is None:
#         raise Exception("DATABASE_URL environment variable not defined")
#     DATABASES = {
#         "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
#     }

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

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
}

# django_heroku.settings(locals())
