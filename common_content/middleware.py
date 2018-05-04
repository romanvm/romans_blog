from django.http import HttpResponse
from django.template.loader import render_to_string
from .utils import get_site_config


def maintenance_mode_middleware(get_response):
    """
    Send HTTP 503 response if site maintenance mode is enabled
    """
    def middleware(request):
        site_config = get_site_config()
        if (site_config.maintenance_mode and
                not request.user.is_authenticated and
                not request.path.startswith('/admin')):
            return HttpResponse(
                render_to_string('503.html', context={'site_name': site_config.site_name}),
                status=503
            )
        return get_response(request)
    return middleware
