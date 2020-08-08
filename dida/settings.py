"""
Django settings for dida project.
Generated by 'django-admin startproject' using Django 3.0.5.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import django_heroku
import dj_database_url 
from boto.s3.connection import S3Connection

try:
    s3 = S3Connection(os.environ['SENDGRID_PASSWORD'], os.environ['KEY'] )
    SECRET_KEY = os.getenv('KEY')
    EMAIL_HOST_USER = 'apikey'  
    EMAIL_HOST_PASSWORD =os.getenv('SENDGRID_PASSWORD')

    SECRET_KEY = os.getenv('KEY')
except:
    from secrets_folder import secrets
    SECRET_KEY = secrets.KEY
    EMAIL_HOST_USER = 'apikey'  
    EMAIL_HOST_PASSWORD =secrets.SENDGRID_PASSWORD





# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#get the heroku config variables if it throws an error
#that means we are running it locally
#so it now uses local values from the secret folder

    


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['didalens.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'didaup',
    'users',
    'crispy_forms'
]
whitenoise='whitenoise.middleware.WhiteNoiseMiddleware'
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dida.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'dida.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': 
    {'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'didalens',
    'USER': 'adminmaster',
    'PASSWORD': 'adminmaster',
    'HOST': 'localhost',
    'PORT': '',
    }
    }
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db',
    }
}

'''
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


AUTH_USER_MODEL='users.CustomUser'

LOGIN_REDIRECT_URL='/goals/'

#EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
#EMAIL_FILE_PATH=os.path.join(BASE_DIR, 'sent_emails')

'''

# Amazon ses
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
'''


#sendgrid
EMAIL_HOST ='smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


'''check the upperpart of the file for the remining credentials'''
# Activate Django-Heroku.
django_heroku.settings(locals())


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
STATIC_ROOT  =   os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'static'),
)
#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)


