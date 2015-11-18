import os
from django.shortcuts import render
from django.conf import settings


def index(request):
    """
    Blog index view
    """
    context = {'title': 'Roman\'s Blog', 'path': request.path}
    return render(request, os.path.join(settings.CURRENT_SKIN, 'posts_list.html'), context)
