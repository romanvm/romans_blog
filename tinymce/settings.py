from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage


PROFILE = getattr(settings, 'TINYMCE_PROFILE', 'default')
CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', {})

if getattr(settings, 'TINYMCE_JS_URL', False):
    raise DeprecationWarning('TINYMCE_JS_URL is not supported anymore, check docs for instructions.')
JS_URL = staticfiles_storage.url('tinymce/tinymce.min.js')
JS_ROOT = staticfiles_storage.url('tinymce')
JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]

CSS_URL = getattr(settings, 'TINYMCE_CSS_URL', staticfiles_storage.url('tiny_mce/tinymce4.css'))

if getattr(settings, 'TINYMCE_COMPRESSOR', False):
    raise NotImplementedError('TINYMCE_COMPRESSOR is not implemented yet.')
USE_COMPRESSOR = False

CALLBACKS = getattr(settings, 'TINYMCE_CALLBACKS', {})
USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)
USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER', False)
USE_CODESAMPLE = getattr(settings, 'TINYMCE_CODESAMPLE', False)
USE_OLD_PREVIEW = getattr(settings, 'TINYMCE_OLD_PREVIEW', False)
