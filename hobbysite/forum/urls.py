from django.urls import path
from forum.views import ThreadListView, ThreadDetailView

urlpatterns = [
    path('threads/', PostListView.as_view(), name='posts_list'),
    path('thread/<int:pk>/', PostDetailView.as_view(), name='post_showcase'),
    ]

app_name = 'forum'
