from django.urls import path
from wiki.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('wiki/articles', ArticleListView.as_view(), name='article-list'),
    path('wiki/article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]

app_name='wiki'