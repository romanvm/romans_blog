# coding: utf-8
"""
Django settings for romans_blog project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from importlib import import_module

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fvh+o&w4qo-afc#fu8fy7=1_imte!d7k1d)9q+=603@963+sk!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = (
    'filebrowser',
    'tinymce',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'haystack',
    'blog',
    'pages',
    'cerulean_skin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'romans_blog.urls'

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

WSGI_APPLICATION = 'romans_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGES = [
    ('en-us', 'US English'),
    ('uk', 'Українська'),
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files (user images, videos, other files)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# TinyMCE settings

TINYMCE_PROFILE = 'custom'
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'modern',
    'plugins': 'compat3x advlist autolink link image imagetools lists charmap print preview hr anchor pagebreak '
               'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media '
               'nonbreaking save table contextmenu directionality emoticons template paste textcolor '
               'preview3 codesample spellchecker autosave django_saveandcontinue',
    'toolbar1': 'django_saveandcontinue | undo redo | cut copy paste | searchreplace | styleselect removeformat | '
                'fontselect fontsizeselect | forecolor backcolor | code preview | spellchecker | fullscreen',
    'toolbar2': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify '
                '| bullist numlist outdent indent | blockquote hr charmap nonbreaking '
                '| link anchor | image media emoticons | table | codesample',
    'contextmenu': 'formats | cut copy paste | link image | inserttable row cell',
    'style_formats': [
        {'title': 'Special', 'items': [
            {'title': 'Small text', 'inline': 'small'},
            {'title': 'Inline code', 'inline': 'code'},
            {'title': 'Keyboard input', 'inline': 'kbd'},
            {'title': 'Sample output', 'inline': 'samp'},
        ]},
        {'title': 'Image', 'items': [
            {'title': 'Image Left', 'selector': 'img', 'styles': {'float': 'left', 'margin': '10px'}},
            {'title': 'Image Right', 'selector': 'img', 'styles': {'float': 'right', 'margin': '10px'}}
        ]},
    ],
    'style_formats_merge': True,
    'width': 960,
    'height': 480,
    'spellchecker_languages': 'English (US)=en_US,Russian=ru,Ukrainian=uk',
    'spellchecker_language': 'en_US',
    'plugin_preview_width': 840,
    'plugin_preview_height': 600,
    'plugin_preview_pageurl': '/tinymce-preview/',
    'image_advtab': True,
    'default_link_target': '_blank',
}
TINYMCE_FILEBROWSER = True
TINYMCE_SPELLCHECKER = True

# Skin settings

CURRENT_SKIN = 'cerulean_skin'
skin_settings = import_module('{0}.settings'.format(CURRENT_SKIN))
image_class_list = getattr(skin_settings, 'IMAGE_CLASS_LIST', None)
TINYMCE_DEFAULT_CONFIG['image_class_list'] = image_class_list
table_class_list = getattr(skin_settings, 'TABLE_CLASS_LIST', None)
TINYMCE_DEFAULT_CONFIG['table_class_list'] = table_class_list
table_row_class_list = getattr(skin_settings, 'TABLE_ROW_CLASS_LIST', None)
TINYMCE_DEFAULT_CONFIG['table_row_class_list'] = table_row_class_list

# Haystack search settings

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

# Enable this if your server has enough power to update index on every save
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# === Custom site settings ===

SITE_ID = 1
SITE_NAME = 'Roman\'s Blog'
BLOG_POSTS_PAGINATE_BY = 5
BLOG_SIDEBAR_POSTS_COUNT = 3
BLOG_SIDEBAR_MONTHS_COUNT = 5
# Provide a Disqus shortname to enable post comments
DISQUS_SHORTNAME = ''
# Provide a Google Analytics ID to enable your web-site usage tracking
GOOGLE_ANALYTICS_ID = ''

# ============================

# Load production settings if any
try:
    from .local_settings import *
except ImportError:
    pass
