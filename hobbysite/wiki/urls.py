from django.urls import path
from wiki.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/add/', ArticleCreateView.as_view(), name="article-form"),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name="article-update")
]

app_name='wiki'