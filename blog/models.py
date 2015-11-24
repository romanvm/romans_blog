from django.db import models
from django.utils.translation import ugettext
from django.utils.text import slugify
from django.utils.timezone import now
from filebrowser.fields import FileBrowseField
from tinymce.models import HTMLField
from unidecode import unidecode

_ = ugettext


class Category(models.Model):
    """
    Represents a blog posts category
    """
    name = models.CharField(verbose_name=_('Category Name'), max_length=100, unique=True)
    # Translators: The last part of a web-page URL, usually derives from the page title, e.g. /about-us/
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, unique=True)

    def __str__(self):
        return self.name

    def clean(self):
        # Auto-populate sluf field
        if not self.slug:
            self.slug = slugify(unidecode(self.name))

    class Meta:
        verbose_name = _('Category')
        # Translators: General plural without a number
        verbose_name_plural = _('Categories')
        ordering = ['name']


class Post(models.Model):
    """
    Represents a blog post
    """
    title = models.CharField(verbose_name=_('Title'), max_length=200, db_index=True)
    date_published = models.DateField(verbose_name=_('Date Published'), blank=True, null=True)
    date_updated = models.DateField(verbose_name=_('Date Updated'), blank=True, null=True)
    # Translators: The last part of a web-page URL, usually derives from the page title, e.g. /about-us/
    slug = models.SlugField(verbose_name=_('Slug'), max_length=200)
    categories = models.ManyToManyField(Category, verbose_name=_('Categories'), related_name='posts', blank=True)
    # Translators: A cover picture for a blog post that represents its contents in some way.
    cover_image = FileBrowseField(_('Cover Image'), max_length=200, extensions=['.jpg', '.png', '.gif'],
                                     blank=True, null=True)
    is_published = models.BooleanField(verbose_name=_('Published'), default=False)
    is_featured = models.BooleanField(verbose_name=_('Featured'), default=False)
    allow_comments = models.BooleanField(verbose_name=_('Allow comments'), default=True)
    content = HTMLField(verbose_name=_('Post Content'))

    def __str__(self):
        return self.title

    def clean(self):
        if self.is_published:
            # Auto-pupulate date_published for a newly published post
            if not self.date_published:
                self.date_published = now()
            # Auto-pupulate date_updated for an edited published post
            elif self.date_published and not self.date_updated:
                self.date_updated = now()


    class Meta:
        verbose_name = _('Post')
        # Translators: General plural without a number
        verbose_name_plural = _('Posts')
        ordering = ['-date_published', '-pk']
