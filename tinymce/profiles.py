from tinymce import settings

DEFAULT = {
    'theme': 'modern',
    'plugins': 'compat3x advlist autolink link image lists charmap print preview hr anchor pagebreak '
               'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media '
               'nonbreaking save table contextmenu directionality emoticons template paste textcolor codesample',
    'toolbar': 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | '
               'bullist numlist outdent indent | link image media emoticons | print preview fullpage | '
               'forecolor backcolor',
}

SIMPLE = {
    'theme': 'modern',
    'plugins': '',
    'toolbar': 'bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link', 
    'menubar': False,
    'inline': True,
    'add_unload_trigger': False,
    'schema': 'html5',
    'statusbar': True,
}

if settings.USE_CODESAMPLE:
    DEFAULT['toolbar'] += ' | codesample'
if settings.USE_SPELLCHECKER:
    DEFAULT['plugins'] += ' spellchecker'
    DEFAULT['toolbar'] += ' | spellchecker'
    DEFAULT['spellchecker_languages'] = 'English (US)=en_US,English (UK)=en_UK,French=fr_FR,German=de_DE'
    DEFAULT['spellchecker_language'] = 'en_US'
