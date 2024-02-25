import environ

from pathlib import Path
import os
from datetime import timedelta
import ssl

env = environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG") == "True"

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'djoser',
    "rest_framework_simplejwt",
    'corsheaders',
    'core'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    },
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
 
    'DEFAULT_AUTHENTICATION_CLASSES': (
   
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

}


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = 'media/'


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_USE_TLS = True
EMAIL_TLS_VERSION = ssl.PROTOCOL_TLS

EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = env("EMAIL_HOST_USER")
SERVER_EMAIL = env("EMAIL_HOST_USER")
AUTH_USER_MODEL = "core.User"


SITE_NAME = env('DOMAIN')


DJOSER = {
    "USER_CREATE_PASSWORD_RETYPE": True,
    'PASSWORD_RESET_CONFIRM_URL': 'reset_password/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'EMAIL': {
        'password_reset': 'core.custom_reset_email.CustomPasswordResetEmail'
    }
}
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000"
]



SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=90),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
}



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
