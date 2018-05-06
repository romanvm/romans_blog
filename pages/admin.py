from django.contrib import admin
from filebrowser.settings import ADMIN_THUMBNAIL
from adminsortable2.admin import SortableAdminMixin
from .models import Page, MenuLink


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'keywords', 'last_updated', 'meta_description', 'image_thumbnail')
    fields = ('title', 'keywords', 'last_updated', 'content', 'featured_image', 'meta_description')
    readonly_fields = ('last_updated',)
    search_fields = ('title',)
    save_on_top = True

    def image_thumbnail(self, obj):
        if obj.featured_image:
            return '<img src="{0}" width="105" height="45">'.format(
                obj.featured_image.url
            )
        else:
            return ''

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = 'Featured Image'


@admin.register(MenuLink)
class MenuLinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    """
    Admin for Menu Links
    """
    list_display = ('caption', 'slug', 'page', 'show_side_panel')
    list_editable = ('page', 'show_side_panel')
    prepopulated_fields = {'slug': ('caption',)}
