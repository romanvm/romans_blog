from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.utils.translation import ugettext
from django.shortcuts import get_object_or_404
from .models import Post, Category

_ = ugettext


class _PostsListView(ListView):
    """
    Base class for displaying post lists
    """
    template_name = '{0}/blog_posts_list.html'.format(settings.CURRENT_SKIN)
    context_object_name = 'posts'
    paginate_by = settings.BLOG_POSTS_PAGINATE_BY
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


class BlogFeaturedPostsView(_PostsListView):
    """
    Displays the list of featured posts
    """
    queryset = Post.objects.filter(is_published=True, is_featured=True)
    page_title = _('Featured Posts')


class BlogCategoryView(_PostsListView):
    """
    Displays the list of posts in a given category
    """

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        self.page_title = _('Posts in category "{0}"'.format(category.name))
        return Post.objects.filter(is_published=True, categories__pk=category.pk)


class BlogPostView(DetailView):
    """
    Displays a blog post page
    """
    template_name = '{0}/blog_post.html'.format(settings.CURRENT_SKIN)
    queryset = Post.objects.filter(is_published=True)
    context_object_name = 'post'
    query_pk_and_slug = True
