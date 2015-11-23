from django.contrib import admin
from .models import Page, MenuLink


class MenuLinkAdmin(admin.ModelAdmin):
    """
    Admin for Menu Links
    """
    list_display = ('caption', 'slug', 'page')
    list_filter = ['page']


admin.site.register(Page)
admin.site.register(MenuLink, MenuLinkAdmin)
