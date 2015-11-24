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
from django.views.generic import RedirectView
from filebrowser.sites import site
from .views import tinymce_skinned_preview

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^tinymce-preview/(?P<skin_name>.+)/$', tinymce_skinned_preview, name='tinymce_skinned_preview'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^$', RedirectView.as_view(pattern_name='blog:blog_index', permanent=False)),
    url(r'', include('pages.urls', namespace='pages')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
