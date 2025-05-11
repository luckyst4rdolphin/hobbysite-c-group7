from django.urls import path
from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView

urlpatterns = [
   path('articles/', ArticleListView.as_view(), name="article-list"),
   path('article/<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
   path('article/add/', ArticleCreateView.as_view(), name="article-form"),
]

app_name = "blog"