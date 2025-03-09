from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from blog.models import ArticleCategory, Article

class ArticleCategoryListView(ListView):
    context_object_name = "categories"
    queryset = ArticleCategory.objects.all().order_by('name')
    template_name = 'article_category_list.html'



