from django.shortcuts import render


def index(request):
    """
    Blog index view
    """
    context = {'title': 'Roman\'s Blog', 'path': request.path}
    return render(request, 'blog/index.html', context)
