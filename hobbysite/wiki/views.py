from django.shortcuts import render
from django.views.generic import ListView, DetailView
from wiki.models import Article

# Create your views here.
class ArticleListView(ListView):
    context_object_name = 'articles'
    queryset = Article.objects.all().order_by('-created_on')
    template_name = 'article_categories.html'

class ArticleDetailView(ListView):
    context_object_name = 'article'
    model = Article
    template_name = 'article.html'

