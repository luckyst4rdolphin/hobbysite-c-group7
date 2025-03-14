from django.views.generic import ListView, DetailView
from forum.models import PostCategory, Post


class PostListView(ListView):
    """
    A view that displays all categories, together with their respective threads.
    """

    context_object_name = 'posts'
    queryset = Post.objects.all()
    template_name = 'post_list.html'

    
    def get_context_data(self, **kwargs):
        """
        Adds thread categories to the context.
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = PostCategory.objects.all()
        return context


class PostDetailView(DetailView):
    """
    Displays details of a single thread.
    """
    context_object_name = "post"
    model = Post
    template_name = 'post.html'
