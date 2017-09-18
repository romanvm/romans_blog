from django.contrib import admin
from .models import Page, MenuLink


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'keywords', 'last_updated', 'meta_description')
    fields = ('title', 'keywords', 'last_updated', 'content', 'meta_description')
    readonly_fields = ('last_updated',)
    search_fields = ('title',)
    save_on_top = True


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    """
    Admin for Menu Links
    """
    list_display = ('caption', 'slug', 'show_side_panel', 'page')
    list_editable = ('page',)
    prepopulated_fields = {'slug': ('caption',)}
