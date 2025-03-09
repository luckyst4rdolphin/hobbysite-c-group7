from django.urls import path
from blog.views import ArticleCategoryListView

urlpatterns = [
    path('blog/articles', ArticleCategoryListView.as_view(), name="acrticle-category-list"),
]

app_name = "blog"