from django.views.generic.detail import DetailView
from django.conf import settings
from .models import MenuLink


class PageView(DetailView):
    template_name = '{0}/page.html'.format(settings.CURRENT_SKIN)
    queryset = MenuLink.objects.exclude(page=False)
    context_object_name = 'menu_link'
