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
from django.contrib.sitemaps.views import sitemap
from django.utils.translation import ugettext as _
from django.db.utils import DatabaseError
from filebrowser.sites import site
from blog.sitemaps import BlogPostsSiteMap
from pages.sitemaps import PagesSiteMap
from common_content.utils import get_site_config
from common_content.views import robots_txt

sitemaps = {
    'blog': BlogPostsSiteMap,
    'pages': PagesSiteMap,
            }
try:
    # Translators: The placeholder represents a site's name
    admin.site.site_header = _('{0} Administration').format(get_site_config().site_name)
except DatabaseError:  # This is to run migrate when site_config table has not been created yet.
    pass

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$', robots_txt, name='robots'),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^pages/', include('pages.urls', namespace='pages')),
    url(r'', include('blog.urls', namespace='blog')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.insert(0, url(r'^__debug__/', include(debug_toolbar.urls)))
