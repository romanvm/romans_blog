import os
from django.shortcuts import render
from django.conf import settings
from django.template import RequestContext, loader
from django.http import HttpResponse


def index(request):
    """
    Blog index view
    """
    context = {'title': 'Roman\'s Blog', 'path': request.path}
    return render(request, os.path.join(settings.CURRENT_SKIN, 'posts_list.html'), context)


def tinymce_preview(request, skin_name):
    """
    Returns a HttpResponse whose content is an HTML file that is used
    by the TinyMCE preview plugin. The template is loaded from '<skin_name>/tinymce_preview.html'.
    """
    template_files = ('{0}/tinymce_preview.html'.format(skin_name),)
    template = loader.select_template(template_files)
    return HttpResponse(template.render(RequestContext(request)), content_type="text/html")
