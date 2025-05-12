from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import ModelFormMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import Article, ArticleCategory, Comment
from user_management.models import Profile
from .forms import ArticleForm, CommentForm
from django.urls import reverse_lazy

class ArticleListView(ListView):
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

class ArticleDetailView(DetailView, ModelFormMixin):
    '''
    Creates a base view for displaying the complete article.
    '''
    context_object_name = "article"
    model = Article
    template_name = 'article.html'
    form_class = CommentForm
    initial = {'entry':'Say something'}

    def get_success_url(self):
        return reverse_lazy('blog:article-detail', kwargs={'pk': self.object.article.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('-created_on')
        context['comment_form'] = context['form']
        context['comments'] = Comment.objects.filter(article=self.object)
        context['user'] = self.request.user
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.article = self.object
        new_comment.author = self.request.user.profile
        new_comment.save()
        return super(ArticleDetailView, self).form_valid(form)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    '''
    Creates base view for new article form.
    '''
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
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    '''
    Creates base view for updating an article.
    '''
    model = Article
    template_name = "article_form.html"
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy('blog:article-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleUpdateView, self).get_context_data(**kwargs)
        context['article_form'] = context['form']
        return context