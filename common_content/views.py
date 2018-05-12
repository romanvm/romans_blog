from django.http import HttpResponse
from .utils import get_site_config


def robots_txt(request):
    """
    Returns robots.txt for the site
    """
    site_config = get_site_config()
    return HttpResponse(site_config.robots_txt, content_type='text/plain')
