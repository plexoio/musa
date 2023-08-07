"""
Django settings for django_musa project.

Generated by 'django-admin startproject' using Django 3.2.20.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# import cloudinary
from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = [
    os.path.join('templates'),
    os.path.join('templates/frontend'),
    os.path.join('templates/account'),
    os.path.join('templates/backend/user-dashboard'),
    os.path.join('templates/backend/admin-dashboard'),
]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')
development = os.environ.get('DEVELOPMENT', False)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if development:
    ALLOWED_HOSTS = ['8000-plexoio-musa-327b9ltgdbq.ws-eu102.gitpod.io',
                     os.environ.get('HEROKU_HOSTNAME')]
else:
    ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'django_summernote',
    'musa',
    'authentication',
    'user_profile',
    'vote_management',
    'admin_profile'
]

# Account Management

ACCOUNT_FORMS = {
    'signup': 'musa.forms.CustomSignupForm',
}

AUTH_USER_MODEL = 'musa.UserProfile'
SITE_ID = 1

LOGIN_REDIRECT_URL = 'role_redirect'
LOGOUT_REDIRECT_URL = '/login/'

ACCOUNT_LOGIN_ON_SIGNUP = True
ACCOUNT_LOGIN_REDIRECT_URL = 'role_redirect'
ACCOUNT_EMAIL_VERIFICATION = 'none'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_musa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIR,
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

WSGI_APPLICATION = 'django_musa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if development:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:

    DATABASES = {'default': dj_database_url.parse(
        os.environ.get("DATABASE_URL"))
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    BASE_DIR / 'static' / 'admin',
    BASE_DIR / 'static' / 'custom',
    BASE_DIR / 'static' / 'font',
    BASE_DIR / 'static' / 'homepage',
    BASE_DIR / 'static' / 'user',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
