from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Article

class ArticleListView(ListView):
    context_object_name = "articles"
    queryset = Article.objects.all().order_by('-created_on')
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    context_object_name = "article"
    model = Article
    template_name = 'article.html'

