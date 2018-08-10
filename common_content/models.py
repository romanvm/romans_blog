from django.db import models
from django.utils.translation import ugettext as _
from solo.models import SingletonModel
from filebrowser.fields import FileBrowseField


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(_('Site Name'), max_length=256, default='Roman\'s Blog')
    site_tagline = models.CharField(_('Site Tagline'), max_length=256, blank=True)
    site_logo = FileBrowseField(_('Site Logo'), max_length=1024,
                                extensions=['.png'], blank=True)
    featured_image = FileBrowseField(verbose_name=_('Featured Image'), max_length=1024,
                                     extensions=['.jpg', '.jpeg', '.png'], blank=True)
    disqus_shortname = models.CharField(_('Disqus Shortname'), max_length=64, blank=True)
    google_analytics_id = models.CharField(_('Google Analytics ID'), max_length=64, blank=True)
    facebook = models.CharField(_('Facebook Profile'), max_length=256, blank=True)
    twitter = models.CharField(_('Twitter Profile'), max_length=256, blank=True)
    linkedin = models.CharField(_('LinkedIn Profile'), max_length=256, blank=True)
    github = models.CharField(_('GitHub Profile'), max_length=256, blank=True)
    stackoverflow = models.CharField(_('Stackoverflow Profile'), max_length=256, blank=True)
    maintenance_mode = models.BooleanField(_('Maintenance Mode'), default=False)
    robots_txt = models.TextField('robots.txt', blank=True,
                                  default='User-agent: *\n'
                                          'Disallow: /admin\n'
                                          'Disallow: /search')

    def __str__(self):
        return _('Site Configuration')

    class Meta:
        verbose_name = _('Site Configuration')
