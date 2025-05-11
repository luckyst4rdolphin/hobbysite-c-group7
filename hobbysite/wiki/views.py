from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from wiki.models import Article, ArticleCategory, Comment
from .forms import ArticleCreateForm, ArticleUpdateForm
from user_management.models import Profile

class ArticleListView(ListView):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class is the class-based list view for the Article.

    '''    
    context_object_name = 'articles'
    queryset = Article.objects.all().order_by('-created_on')
    template_name = 'article_categories.html'

    def get_context_data(self, **kwargs):
        '''
        @fn get_context_data
        @brief returns context_data of the article
        '''
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all().order_by('name')
        context['user'] = self.request.user
        context['profile'] = Profile.objects.all
        return context

class ArticleDetailView(DetailView):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class is the class-based detail view for the Article.

    '''    
    context_object_name = 'article'
    model = Article
    template_name = 'wiki_article.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class contains the form view for adding new Articles.

    '''    
    model = Article
    template_name = 'article_form.html'
    form_class = ArticleCreateForm
    success_url = '/wiki/article/add'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['article_form'] = context['form']
        return context

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class contains the form view for updating existing
    Articles.

    '''    
    model = Article
    template_name = 'article_update_form.html'
    form_class = ArticleUpdateForm
    success_url = '/wiki/article/add'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['article_update_form'] = context['form']
        return context