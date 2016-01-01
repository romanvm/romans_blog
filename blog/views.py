from datetime import date
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.utils.translation import ugettext
from django.utils.dateformat import format as format_date
from django.shortcuts import get_object_or_404
from django.http import Http404
from haystack.generic_views import SearchView
from .models import Post, Category

_ = ugettext


class _PostsListView(ListView):
    """
    Base class for displaying post lists
    """
    template_name = '{0}/blog_posts_list.html'.format(settings.CURRENT_SKIN)
    context_object_name = 'posts'
    paginate_by = settings.BLOG_POSTS_PAGINATE_BY


class _PageTitleMixIn:
    """
    Adds page_title to ListView's context
    """
    page_title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class BlogHomeView(_PostsListView):
    """
    Displays the list of all published posts starting from the recent.
    """
    queryset = Post.objects.filter(is_published=True)


class BlogFeaturedPostsView(_PageTitleMixIn, _PostsListView):
    """
    Displays the list of featured posts
    """
    queryset = Post.objects.filter(is_published=True, is_featured=True)
    page_title = _('Featured Posts')


class BlogCategoryView(_PageTitleMixIn, _PostsListView):
    """
    Displays the list of posts in a given category
    """

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        self.page_title = _('Posts in "{0}" category'.format(category.name))
        return Post.objects.filter(is_published=True, categories__pk=category.pk)


class BlogCategoriesListView(_PageTitleMixIn, ListView):
    """
    Displays the list of categories that have posts in them
    """
    template_name = '{0}/blog_categories_list.html'.format(settings.CURRENT_SKIN)
    queryset = Category.objects.exclude(posts=None)
    page_title = _('Categories')
    context_object_name = 'categories'


class BlogPostView(DetailView):
    """
    Displays a blog post page
    """
    template_name = '{0}/blog_post.html'.format(settings.CURRENT_SKIN)
    model = Post
    context_object_name = 'post'
    query_pk_and_slug = True

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Prevent non-authenticated users from viewing unpublished posts
        """
        post = super().get_object(queryset)
        if not(post.is_published or self.request.user.is_authenticated()):
            raise Http404
        return post


class BlogArhiveView(_PageTitleMixIn, ListView):
    """
    Displays the blog archive by years and months
    """
    template_name = '{0}/blog_archive.html'.format(settings.CURRENT_SKIN)
    queryset = Post.objects.filter(is_published=True).dates('date_published', 'month', order='DESC')
    context_object_name = 'months'
    page_title = _('Blog Archive')


class BlogMonthArchiveView(_PageTitleMixIn, _PostsListView):
    """
    Displays the list of posts by year and month
    """
    def get_queryset(self):
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])
        self.page_title = _('Blog Archive, {0}').format(format_date(date(year=year, month=month, day=1), 'F Y'))
        return Post.objects.filter(is_published=True, date_published__year=year, date_published__month=month)


class BlogPostSearchView(SearchView):
    template_name = '{0}/blog_search.html'.format(settings.CURRENT_SKIN)
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().highlight()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
