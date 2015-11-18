from django.db import models
from django.utils.translation import ugettext
from tinymce import models as tinymce

_ = ugettext


class Page(models.Model):
    """
    Represents a rich-text page that is not a blog post, e.g 'About me'
    """
    title = models.CharField(verbose_name=_('Page Title'), max_length=200)
    content = tinymce.HTMLField(verbose_name=_('Page Content'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Page')
        #Translators: General plural without a number
        verbose_name_plural = _('Pages')
        ordering = ['title']
