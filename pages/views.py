import os
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import MenuLink


def page_view(request):
    """
    Display Page content
    """
    path = request.path
    link = get_object_or_404(MenuLink, path=path)
    context = {'path': path,
               'title': link.page.title,
               'keywords': link.page.keywords,
               'content': link.page.content,
               }
    template = os.path.join(settings.CURRENT_SKIN, 'page.html')
    return render(request, template, context)
