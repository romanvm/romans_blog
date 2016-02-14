# coding: utf-8
# Module: search_indexes
# Created on: 31.12.2015
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua

from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Haystack Post search index
    """
    text = indexes.CharField(document=True, use_template=True)
    date_published = indexes.DateField(model_attr='date_published', null=True)
    is_featured = indexes.BooleanField(model_attr='is_featured')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.published()
