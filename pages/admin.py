from django.contrib import admin
from .models import Page, MenuLink


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'keywords')
    search_fields = ('title',)
    save_on_top = True


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    """
    Admin for Menu Links
    """
    list_display = ('caption', 'slug', 'page')
    prepopulated_fields = {'slug': ('caption',)}
