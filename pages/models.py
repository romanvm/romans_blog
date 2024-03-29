from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _
from filebrowser.fields import FileBrowseField
from tinymce import models as tinymce


class Page(models.Model):
    """
    Represents a rich-text page that is not a blog post, e.g 'About me'
    """
    title = models.CharField(verbose_name=_('Page Title'), max_length=200)
    keywords = models.CharField(verbose_name=_('Keywords'), max_length=200, blank=True)
    content = tinymce.HTMLField(verbose_name=_('Page Content'))
    last_updated = models.DateTimeField(verbose_name=_('Last Updated'), auto_now=True)
    featured_image = FileBrowseField(verbose_name=_('Featured Image'), max_length=1024,
                                     extensions=['.jpg', '.jpeg', '.png'], blank=True)
    meta_description = models.TextField(verbose_name=_('Description'), max_length=160, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Page')
        #Translators: General plural without a number
        verbose_name_plural = _('Pages')
        ordering = ('title',)


class MenuLinkQuerySet(models.QuerySet):
    """Custom QuerySet for MenuLinks"""
    def have_pages(self):
        """Get MenuLinks that have attached pages"""
        return self.filter(page__isnull=False)


class MenuLink(models.Model):
    """
    Represents a link in the site navigation menu
    """
    caption = models.CharField(verbose_name=_('Caption'), max_length=200)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=200, unique=True)
    page = models.ForeignKey(Page, verbose_name=_('Page'), blank=True, null=True,
                             on_delete=models.CASCADE)
    show_side_panel = models.BooleanField(verbose_name=_('Show side Panel'), default=False)
    position = models.PositiveIntegerField(verbose_name=_('Position'), default=0, blank=False, null=False)
    objects = MenuLinkQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('pages:page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _('Menu Link')
        verbose_name_plural = _('Menu Links')
        ordering = ('position',)
