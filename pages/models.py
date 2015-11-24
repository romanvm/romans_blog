from django.db import models
from django.utils.translation import ugettext
from tinymce import models as tinymce

_ = ugettext


class Page(models.Model):
    """
    Represents a rich-text page that is not a blog post, e.g 'About me'
    """
    title = models.CharField(verbose_name=_('Page Title'), max_length=200)
    keywords = models.CharField(verbose_name=_('Keywords'), max_length=200, blank=True)
    content = tinymce.HTMLField(verbose_name=_('Page Content'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Page')
        #Translators: General plural without a number
        verbose_name_plural = _('Pages')
        ordering = ['title']


class MenuLink(models.Model):
    """
    Represents a link in the site navigation menu
    """
    caption = models.CharField(verbose_name=_('Caption'), max_length=200)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=200, unique=True)
    page = models.ForeignKey(Page, verbose_name=_('Page'), blank=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _('Menu Link')
        verbose_name_plural = _('Menu Links')
        ordering = ['pk']
