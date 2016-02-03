from django.contrib.staticfiles.storage import staticfiles_storage
from tinymce import settings

DEFAULT = {
    'theme': 'modern',
    'plugins': 'compat3x advlist autolink link image lists charmap print preview hr anchor pagebreak '
               'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media '
               'nonbreaking save table contextmenu directionality emoticons template paste textcolor',
    'toolbar1': 'undo redo | styleselect removeformat | fontselect fontsizeselect | forecolor backcolor '
                '| code preview',
    'toolbar2': 'bold italic underline | alignleft aligncenter alignright alignjustify '
                '| bullist numlist outdent indent | blockquote hr charmap '
                '| link image media emoticons',
    'contextmenu': 'formats | link image inserttable | cut copy paste',
    'height': 360,
    'plugin_preview_width': 640,
}

if settings.USE_CODESAMPLE:
    DEFAULT['plugins'] += ' codesample'
    DEFAULT['toolbar2'] += ' | codesample'
if settings.USE_SPELLCHECKER:
    DEFAULT['plugins'] += ' spellchecker'
    DEFAULT['toolbar1'] += ' | spellchecker'
    DEFAULT['spellchecker_languages'] = 'English (US)=en_US,English (UK)=en_UK,French=fr_FR,German=de_DE'
    DEFAULT['spellchecker_language'] = 'en_US'
if settings.USE_OLD_PREVIEW:
    DEFAULT['plugins'] += ' preview3'
    DEFAULT['plugin_preview_pageurl'] = staticfiles_storage.url('tiny_mce/preview3.html')
else:
    DEFAULT['plugins'] += ' preview'

SIMPLE = {
    'theme': 'modern',
    'plugins': '',
    'toolbar': 'bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link', 
    'menubar': False,
    'inline': False,
    'add_unload_trigger': False,
    'schema': 'html5',
    'statusbar': True,
    'height': 360,
}
