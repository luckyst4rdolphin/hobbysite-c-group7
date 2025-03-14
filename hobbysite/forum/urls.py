from django.urls import path
from forum.views import PostListView, PostDetailView

urlpatterns = [
    path('forum/threads/', PostListView.as_view(), name='posts_list'),
    path('forum/thread/<int:pk>/', PostDetailView.as_view(), name='post_showcase'),
    ]

app_name = 'forum'
