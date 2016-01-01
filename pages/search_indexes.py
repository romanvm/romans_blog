# coding: utf-8
# Module: search_indexes
# Created on: 01.01.2016
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua

from haystack import indexes
from .models import MenuLink


class MenuLinkIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Haystack Menu Link search index
    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return MenuLink

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(page__isnull=False)
