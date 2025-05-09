from django.views.generic import ListView, DetailView
from blog.models import Article, ArticleCategory

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
        return context

class ArticleDetailView(DetailView):
    '''
    Creates a base view for displaying the complete article.
    '''
    context_object_name = "article"
    model = Article
    template_name = 'article.html'

