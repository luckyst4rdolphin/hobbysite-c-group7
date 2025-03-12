from django.urls import path
from forum.views import PostListView, PostDetailView

urlpatterns = [
    path('threads/', PostListView.as_view(), name='threads'),
]
