from django.db import models
from django.utils.translation import ugettext
from django.core.urlresolvers import reverse

_ = ugettext


class Category(models.Model):
    """
    Represents a blog posts category
    """
    name = models.CharField(verbose_name=_('Category Name'), max_length=100, unique=True)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        # Translators: General plural without a number
        verbose_name_plural = _('Categories')
        ordering = ['name']
