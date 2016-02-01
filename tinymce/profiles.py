from tinymce import settings

DEFAULT = {
    'theme': 'modern',
    'plugins': 'compat3x advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker '
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
