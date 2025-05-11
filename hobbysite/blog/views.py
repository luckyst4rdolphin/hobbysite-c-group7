from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Article, ArticleCategory
from user_management.models import Profile
from .forms import ArticleForm
from django.urls import reverse_lazy

class ArticleListView(LoginRequiredMixin, ListView):
    '''
    Creates a base view for displaying a list of objects.
    '''
    context_object_name = "articles"
    queryset = Article.objects.all().order_by('-created_on')
    template_name = 'article_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all().order_by('name')
        context['user'] = self.request.user
        context['profile'] = Profile.objects.all()
        return context

class ArticleDetailView(LoginRequiredMixin, DetailView):
    '''
    Creates a base view for displaying the complete article.
    '''
    context_object_name = "article"
    model = Article
    template_name = 'article.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = Article
    template_name = "article_form.html"
    form_class = ArticleForm
    success_url = reverse_lazy('blog:article-list')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['article_form'] = context['form']
        return context