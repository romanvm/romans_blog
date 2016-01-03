"""romans_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from filebrowser.sites import site
from blog.sitemaps import BlogPostsSiteMap
from pages.sitemaps import PagesSiteMap

robots_txt = 'User-agent: *\nDisallow: /admin\nDisallow: /search'
sitemaps = {
    'blog': BlogPostsSiteMap,
    'pages': PagesSiteMap,
            }

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^tinymce-preview/$',
        TemplateView.as_view(template_name='{0}/tinymce_preview.html'.format(settings.CURRENT_SKIN)),
        name='tinymce_preview'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$', lambda r: HttpResponse(robots_txt, content_type='text/plain'), name='robots'),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^pages/', include('pages.urls', namespace='pages')),
    url(r'', include('blog.urls', namespace='blog')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
