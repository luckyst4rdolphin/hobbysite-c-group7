from django.views.generic import ListView, DetailView
from wiki.models import Article, ArticleCategory

# Create your views here.
class ArticleListView(ListView):
    context_object_name = 'articles'
    queryset = Article.objects.all().order_by('-created_on')
    template_name = 'article_categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all().order_by('name')
        return context

class ArticleDetailView(DetailView):
    context_object_name = 'article'
    model = Article
    template_name = 'article.html'

