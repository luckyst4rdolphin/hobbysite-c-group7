from django.urls import path
from blog.views import ArticleListView, ArticleDetailView

urlpatterns = [
   path('/articles/', ArticleListView.as_view(), name="acrticle-list"),
   path('/article/<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
]

app_name = "blog"