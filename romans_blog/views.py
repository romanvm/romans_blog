# coding: utf-8
# Module: views
# Created on: 24.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.shortcuts import render


def tinymce_skinned_preview(request, skin_name):
    """
    Returns a HttpResponse whose content is an HTML file that is used
    by the TinyMCE preview plugin. The template is loaded from '<skin_name>/tinymce_preview.html'.

    This view is created here because it does not belong to any app and I don't want to add
    any project-specific features to the custom tinymce app to keep it reusable.
    """
    return render(request, '{0}/tinymce_preview.html'.format(skin_name))
