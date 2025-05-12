from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import ModelFormMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from wiki.models import Article, ArticleCategory, Comment
from .forms import ArticleCreateForm, CommentForm
from user_management.models import Profile
from django.urls import reverse_lazy

class ArticleListView(LoginRequiredMixin, ListView):
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

class ArticleDetailView(LoginRequiredMixin, DetailView):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class is the class-based detail view for the Article.

    '''    
    context_object_name = 'article'
    model = Article
    template_name = 'wiki_article.html'
    form_class = CommentForm
    initial = {'entry':'Add a comment'}

    def get_success_url(self):
        '''
        @fn get_success_url
        @brief returns the url for the article
        '''
        return reverse_lazy('wiki:article-detail', kwargs={'pk': self.object.article.pk})

    def get_context_data(self, **kwargs):
        '''
        @fn get_context_data
        @brief returns the context for the article
        '''
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('-created_on')
        context['comment_form'] = context['form']
        context['comments'] = Comment.objects.filter(article=self.object)
        context['user'] = self.request.user
        return context
    
    def post(self, request, *args, **kwargs):
        '''
        @fn post
        @brief checks whether the form is valid or invalid
        '''
        form = self.get_form()
        self.object = self.get_object()

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
        
    def form_valid(self, form):
        '''
        @fn form_valid
        @brief makes the form valid
        '''
        new_comment = form.save(commit=False)
        new_comment.article = self.object
        new_comment.author = self.request.user.profile
        new_comment.save()
        return super(ArticleDetailView, self).form_valid(form)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class contains the form view for adding new Articles.

    '''    
    model = Article
    template_name = 'article_create_form.html'
    form_class = ArticleCreateForm
    success_url = reverse_lazy('wiki:article-list')

    def form_valid(self, form):
        '''
        @fn form_valid
        @brief makes the form valid
        '''
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        '''
        @fn get_context_data
        @brief returns the context for the article
        '''
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['article_create_form'] = context['form']
        return context

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class contains the form view for updating existing
    Articles.

    '''
    model = Article
    template_name = 'article_create_form.html'
    form_class = ArticleCreateForm

    def get_success_url(self):
        '''
        @fn get_success_url
        @brief returns the url for the article
        '''
        return reverse_lazy('wiki:article-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        '''
        @fn form_valid
        @brief makes the form valid
        '''
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        '''
        @fn get_context_data
        @brief returns the context for the article
        '''
        context = super(ArticleUpdateView, self).get_context_data(**kwargs)
        context['article_create_form'] = context['form']
        return context
