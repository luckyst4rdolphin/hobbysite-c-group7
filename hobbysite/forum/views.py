from django.views.generic import ListView, DetailView
from forum.models import PostCategory, Post


class PostListView(ListView):
    context_object_name = 'posts'
    queryset = Post.objects.all()
    template_name = 'post_list.html'

    # To access & display each categories within PostCategory as well...
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PostCategory.objects.all()
        return context


class PostDetailView(DetailView):
    context_object_name = "post"
    model = Post
    template_name = 'post.html'
