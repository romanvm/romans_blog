from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.utils.translation import ugettext
from .models import Post

_ = ugettext


class _PostsListView(ListView):
    """
    Base class for displaying post lists
    """
    template_name = '{0}/blog_posts_list.html'.format(settings.CURRENT_SKIN)
    context_object_name = 'posts'
    paginate_by = settings.BLOG_POSTS_PAGINATE_BY

    def get_page_title(self):
        """
        Add page title to the posts list, e.g. 'Featured Posts'
        """
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.get_page_title()
        return context


class BlogHomeView(_PostsListView):
    """
    Displays the list of all published posts starting from the recent.
    """
    queryset = Post.objects.filter(is_published=True)


class BlogFeaturedView(_PostsListView):
    """
    Displays the list of featured posts
    """
    queryset = Post.objects.filter(is_published=True, is_featured=True)

    def get_page_title(self):
        return _('Featured Posts')


class BlogPostView(DetailView):
    """
    Displays a blog post page
    """
    template_name = '{0}/blog_post.html'.format(settings.CURRENT_SKIN)
    queryset = Post.objects.filter(is_published=True)
    context_object_name = 'post'
    query_pk_and_slug = True
