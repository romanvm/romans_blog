from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'cover_image', 'is_published', 'is_featured', 'allow_comments')
    fields = ('title', 'slug', 'date_published', 'is_published', 'is_featured', 'allow_comments', 'content',
              'cover_image', 'categories')
    search_fields = ('title', 'date_published', 'categories')
    list_filter = ('date_published', 'is_published', 'is_featured', 'allow_comments')
    filter_horizontal = ('categories',)
    date_hierarchy = 'date_published'
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    list_per_page = 25

