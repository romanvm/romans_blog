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
from django.utils.translation import ugettext_lazy

_ = ugettext_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fvh+o&w4qo-afc#fu8fy7=1_imte!d7k1d)9q+=603@963+sk!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


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
    'bootstrap_skin',
    'paper_skin',
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

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'mode': 'textareas',
    'width': 800,
    'plugins': 'preview,table,autoresize,advimage,emotions,syntaxhl,youtubeIframe',
    'theme_advanced_buttons1': 'bold,italic,underline,strikethrough,|,'
                             'justifyleft,justifycenter,justifyright,justifyfull,|,'
                             'bullist,numlist,|,outdent,indent,|,forecolor,backcolor,|,'
                             'sup,sub,|,hr,|,blockquote,|,syntaxhl,|,help',
    'theme_advanced_buttons2': 'fontselect,fontsizeselect,formatselect,|,link,unlink,anchor,|,'
                             'image,youtubeIframe,|,emotions,|,removeformat,cleanup,|,code,preview',
    'theme_advanced_buttons3': 'cut,copy,paste,|,undo,redo,|,tablecontrols',
    'browser_spellcheck': True,
    'plugin_preview_width': 1024,
    'plugin_preview_height': 640,
    'theme_advanced_font_sizes': '4pt,6pt,8pt,10pt,12pxt,14pxt,16pt,18pt,24pt,36pt,48pt',
    'relative_urls': False,
    'remove_linebreaks': False,
    'autoresize_min_height': 400,
    'extended_valid_elements': 'img[!src|border:0|alt|title|width|height|style]a[name|href|target|title|onclick],'
                               'textarea[cols|rows|disabled|name|readonly|class]'
                               'iframe[src|title|width|height|allowfullscreen|frameborder|class|id],'
                               'object[classid|width|height|codebase|*],param[name|value|_value|*],'
                               'embed[type|width|height|src|*]',
                          }

# Skin settings

CURRENT_SKIN = 'paper_skin'
#TINYMCE_DEFAULT_CONFIG['plugin_preview_pageurl'] = '/tinymce-preview/{0}/'.format(CURRENT_SKIN)
skin_settings = import_module('{0}.settings'.format(CURRENT_SKIN))
try:
    table_styles = skin_settings.TABLE_STYLES
    table_row_styles = skin_settings.TABLE_ROW_STYLES
    theme_advanced_styles = skin_settings.IMG_STYLES
except AttributeError:
    table_styles = table_row_styles = theme_advanced_styles = ''
TINYMCE_DEFAULT_CONFIG['table_styles'] = table_styles
TINYMCE_DEFAULT_CONFIG['table_row_styles'] = table_row_styles
TINYMCE_DEFAULT_CONFIG['theme_advanced_styles'] = theme_advanced_styles

# Haystack search settings

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# === Custom site settings ===

SITE_ID = 1
SITE_NAME = 'Roman\'s Blog'
BLOG_POSTS_PAGINATE_BY = 5
BLOG_SIDEBAR_POSTS_COUNT = 3
BLOG_SIDEBAR_MONTHS_COUNT = 5
DISQUS_SHORTNAME = 'romanvm'

# ============================

# Load production settings if any
try:
    from .local_settings import *
except ImportError:
    pass
