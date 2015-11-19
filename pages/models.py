import re
from django.db import models
from django.utils.translation import ugettext
from django.core.exceptions import ValidationError
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
    path = models.CharField(verbose_name=_('Path'), max_length=200)
    page = models.ForeignKey(Page, verbose_name=_('Page'), blank=True, null=True)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return self.path

    def clean(self):
        """
        Check if the MenuLink path has correct format: '/<letters-dashes-or-numbers>/'
        """
        if re.match(r'/[\w-]+/', self.path) is None:
            raise ValidationError('Path must include only alphanumeric chars and dashes enclosed in forward slashes: /<path>/')

    class Meta:
        verbose_name = _('Menu Link')
        verbose_name_plural = _('Menu Links')
        ordering = ['pk']
