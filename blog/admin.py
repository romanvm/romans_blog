from django.contrib import admin
from django.utils.translation import ugettext as _
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'get_published_posts_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'last_updated', 'is_published', 'is_featured',
                    'allow_comments', 'meta_description', 'image_thumbnail')
    list_editable = ('is_featured', 'allow_comments')
    fields = ('title', 'slug', 'date_published', 'last_updated', 'content', 'is_published',
              'is_featured', 'allow_comments', 'featured_image', 'categories', 'meta_description')
    readonly_fields = ('last_updated',)
    search_fields = ('title', 'date_published', 'categories')
    list_filter = ('date_published', 'is_published', 'is_featured', 'allow_comments')
    filter_horizontal = ('categories',)
    date_hierarchy = 'date_published'
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    list_per_page = 25
    ordering = ('is_published', '-date_published', '-last_updated')

    def image_thumbnail(self, obj):
        if obj.featured_image:
            return '<img src="{0}">'.format(
                obj.featured_image.version_generate('small').url
            )
        else:
            return ''

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = _('Featured Image')
