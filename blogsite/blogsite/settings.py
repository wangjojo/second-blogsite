"""
Django settings for blogsite project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^#3zta1!d-b%a#4q$=6dhpb4&l8!q!ofe@)t@52hlsvf=nc*%+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

AUTHENTICATION_BACKENDS = ('users.views.CustomBackend',)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'blog',
    'operation',
    'xadmin',
    'crispy_forms',
    'captcha',
    'DjangoUeditor',
    'pure_pagination',
]

AUTH_USER_MODEL = 'users.UserProfile'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',
                'blog.home_processor.home_categorys',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogsite',
        'USER':'root',
        'PASSWORD': 'fg498572715',
        #'HOST':'192.168.74.137',
        'HOST': '39.106.131.162',
        'PORT':'3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
#七牛云配置
QINIU_ACCESS_KEY = 'RNowojsv8Ve2loqwf0HbADY4hS_A8fKkBHPH7xNi'
QINIU_SECRET_KEY = '9K6IY38RZlRbGURu_0uYN_51qRxa8IYuzl4AghZD'
QINIU_BUCKET_NAME = 'photo'
QINIU_BUCKET_DOMAIN = 'wangjojo.top/'
QINIU_SECURE_URL = False

#STATICFILES_STORAGE  = 'qiniustorage.backends.QiniuStaticStorage'

PREFIX_URL = 'http://'


STATIC_URL = '/static/'
'''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
    )
'''
STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN + '/media/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'

#邮件设置
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = '1598374497@qq.com'
EMAIL_HOST_PASSWORD = 'ibrajiswkkkpjfjd'
DEFAULT_FROM_EMAIL = '管理员<1598374497@qq.com>'