from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

# Default TinyMCE 4 layout
DEFAULT = {
    'theme': 'modern',
    'plugins': 'compat3x advlist autolink link image lists charmap print preview hr anchor pagebreak '
               'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media '
               'nonbreaking save table contextmenu directionality emoticons template paste textcolor',
    'toolbar1': 'undo redo | styleselect removeformat | fontselect fontsizeselect | forecolor backcolor '
                '| code',
    'toolbar2': 'bold italic underline | alignleft aligncenter alignright alignjustify '
                '| bullist numlist outdent indent | blockquote hr charmap '
                '| link image media emoticons',
    'contextmenu': 'formats | link image inserttable | cut copy paste',
    'height': 360,
    'plugin_preview_width': 640,
}

# Simple TinyMCE 4 layout
SIMPLE = {
    'theme': 'modern',
    'plugins': 'link image',
    'toolbar': 'styleselect | bold italic underline | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | link image',
    'menubar': False,
    'inline': False,
    'add_unload_trigger': False,
    'schema': 'html5',
    'statusbar': True,
    'height': 360,
}

if getattr(settings, 'TINYMCE_JS_URL', False):
    raise DeprecationWarning('TINYMCE_JS_URL is not supported anymore, check docs for instructions.')
JS_URL = staticfiles_storage.url('tinymce/js/tinymce/tinymce.min.js')
JS_ROOT = staticfiles_storage.url('tinymce/js/tinymce')
JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]

CSS_URL = getattr(settings, 'TINYMCE_CSS_URL', staticfiles_storage.url('tinymce/css/tinymce4.css'))

if getattr(settings, 'TINYMCE_COMPRESSOR', False):
    raise NotImplementedError('TINYMCE_COMPRESSOR is not implemented yet.')
USE_COMPRESSOR = False

CALLBACKS = getattr(settings, 'TINYMCE_CALLBACKS', {})
USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)
USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER', False)
USE_CODESAMPLE = getattr(settings, 'TINYMCE_CODESAMPLE', False)
USE_OLD_PREVIEW = getattr(settings, 'TINYMCE_OLD_PREVIEW', False)

CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', {})
profile = getattr(settings, 'TINYMCE_PROFILE', 'default')
if profile == 'default':
    if USE_CODESAMPLE:
        DEFAULT['plugins'] += ' codesample'
        DEFAULT['toolbar2'] += ' | codesample'
    if USE_SPELLCHECKER:
        DEFAULT['plugins'] += ' spellchecker'
        DEFAULT['toolbar1'] += ' | spellchecker'
        DEFAULT['spellchecker_languages'] = 'English (US)=en_US,English (UK)=en_UK,French=fr_FR,German=de_DE'
        DEFAULT['spellchecker_language'] = 'en_US'
    if USE_OLD_PREVIEW:
        DEFAULT['plugins'] += ' preview3'
        DEFAULT['toolbar1'] += ' | preview3'
    else:
        DEFAULT['plugins'] += ' preview'
        DEFAULT['toolbar1'] += ' | preview'
    DEFAULT.update(CONFIG)
    CONFIG = DEFAULT
elif profile == 'simple':
    SIMPLE.update(CONFIG)
    CONFIG = SIMPLE
