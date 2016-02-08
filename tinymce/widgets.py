# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

"""
This TinyMCE widget was copied and extended from this code by John D'Agostino:
http://code.djangoproject.com/wiki/CustomWidgetsTinyMCE
"""
from __future__ import unicode_literals
import sys
if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    import simplejson as json
else:
    import json
import enchant
from django import forms
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.core.urlresolvers import reverse
from django.forms.widgets import flatatt

try:
    from collections import OrderedDict as SortedDict
except ImportError:
    from django.utils.datastructures import SortedDict

try:
    from django.utils.encoding import smart_text as smart_unicode
except ImportError:
    try:
        from django.utils.encoding import smart_unicode
    except ImportError:
        from django.forms.util import smart_unicode

from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.translation import get_language, ugettext as _
from django.template.loader import render_to_string
import tinymce.settings


class TinyMCE(forms.Textarea):
    """
    TinyMCE widget. Set settings.TINYMCE_JS_URL to set the location of the
    javascript file. Default is "MEDIA_URL + 'js/tiny_mce/tiny_mce.js'".
    You can customize the configuration with the mce_attrs argument to the
    constructor.

    In addition to the standard configuration you can set the
    'content_language' parameter. It takes the value of the 'language'
    parameter by default.

    In addition to the default settings from settings.TINYMCE_DEFAULT_CONFIG,
    this widget sets the 'language', 'directionality' and
    'spellchecker_languages' parameters by default. The first is derived from
    the current Django language, the others from the 'content_language'
    parameter.
    """

    def __init__(self, content_language=None, attrs=None, mce_attrs=None, profile=None):
        super(TinyMCE, self).__init__(attrs)
        self.mce_attrs = mce_attrs or {}
        self.content_language = content_language or self.mce_attrs.get('language', None)
        default_profile = tinymce.settings.CONFIG or tinymce.settings.SIMPLE
        self.profile = get_language_config(content_language)
        self.profile.update(profile or default_profile)
        print(self.profile)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        value = smart_unicode(value)
        final_attrs = self.build_attrs(attrs)
        final_attrs['name'] = name
        assert 'id' in final_attrs, "TinyMCE widget attributes must contain 'id'"
        mce_config = self.profile.copy()
        mce_config.update(self.mce_attrs)
        mce_config['selector'] = '#%s' % final_attrs['id']
        mce_json = json.dumps(mce_config, indent=2)
        if mce_config.get('inline', False):
            html = ['<div%s>%s</div>' % (flatatt(final_attrs), escape(value))]
        else:
            html = ['<textarea%s>%s</textarea>' % (flatatt(final_attrs), escape(value))]
        html.append('<script type="text/javascript">%s</script>' % (
            render_to_string('tinymce/default_tinymce_init.js',
                             context={'callbacks': get_tinymce_callbacks(),
                             'tinymce_config': mce_json[1:-1]})))
        return mark_safe('\n'.join(html))

    @property
    def media(self):
        if tinymce.settings.USE_COMPRESSOR:
            js = [reverse('tinymce-compressor')]
        else:
            js = [tinymce.settings.JS_URL]
        if tinymce.settings.USE_FILEBROWSER:
            js.append(reverse('tinymce-filebrowser'))
        css = {'all': [tinymce.settings.CSS_URL]}
        return forms.Media(js=js, css=css)


class AdminTinyMCE(TinyMCE, admin_widgets.AdminTextareaWidget):
    pass


def get_language_config(content_language=None):
    """
    Creates a language configuration for TinyMCE4 based on Django settings

    :param content_language:
    :return: config
    """
    language = (content_language or get_language())[:2]
    config = {'language': language, 'spellchecker_language': ''}
    enchant_languages = enchant.list_languages()
    lang_names = []
    for lang, name in settings.LANGUAGES:
        lang = convert_language_code(lang)
        if lang not in enchant_languages:
            lang = lang[:2]
        if not config['spellchecker_language']:
            config['spellchecker_language'] = lang
        lang_names.append('%s=%s' % (name, lang))
    config['spellchecker_languages'] = ','.join(lang_names)
    if language[:2] in settings.LANGUAGES_BIDI:
        config['directionality'] = 'rtl'
    else:
        config['directionality'] = 'ltr'
    return config


def convert_language_code(django_lang):
    """
    Converts Django language codes "ll-cc" into ISO codes "ll_CC" or "ll"

    :param django_lang:
    :return: iso_lang
    """
    lang_n_country = django_lang.split('-')
    try:
        country = lang_n_country[1].upper()
        return '_'.join((lang_n_country[0], country))
    except IndexError:
        return lang_n_country[0]


def get_tinymce_callbacks():
    """
    Get TinyMCE JS callbacks

    :return: callbacks
    """
    callbacks = tinymce.settings.CALLBACKS
    if (tinymce.settings.USE_FILEBROWSER and
                'file_browser_callback' not in callbacks):
        callbacks['file_browser_callback'] = 'djangoFileBrowser'
    if (tinymce.settings.USE_SPELLCHECKER and
                'spellchecker_callback' not in callbacks):
        callbacks['spellchecker_callback'] = render_to_string('tinymce/spellchecker.js')
    return callbacks
