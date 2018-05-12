from django.db import models
from django.utils.translation import ugettext as _
from solo.models import SingletonModel
from filebrowser.fields import FileBrowseField


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(_('Site Name'), max_length=256, default='Roman\'s Blog')
    site_tagline = models.CharField(_('Site Tagline'), max_length=256, blank=True)
    featured_image = FileBrowseField(verbose_name=_('Featured Image'), max_length=1024,
                                     extensions=['.jpg', '.jpeg', '.png'], blank=True)
    disqus_shortname = models.CharField(_('Disqus Shortname'), max_length=64, blank=True)
    google_analytics_id = models.CharField(_('Google Analytics ID'), max_length=64, blank=True)
    maintenance_mode = models.BooleanField(default=False)
    robots_txt = models.TextField('robots.txt', blank=True,
                                  default='User-agent: *\nDisallow: /admin\nDisallow: /search')

    def __str__(self):
        return _('Site Configuration')

    class Meta:
        verbose_name = _('Site Configuration')
