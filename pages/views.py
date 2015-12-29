from django.conf import settings
from django.views.generic.detail import DetailView
from .models import MenuLink


class PageView(DetailView):
    """
    Show a page
    """
    template_name = '{0}/page.html'.format(settings.CURRENT_SKIN)
    queryset = MenuLink.objects.filter(page__isnull=False)
    context_object_name = 'menu_link'
