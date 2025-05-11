from django.urls import path
from forum.views import ThreadListView, ThreadDetailView

urlpatterns = [
    path('threads/', ThreadListView.as_view(), name='thread-list'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread-detail'),
    path('thread/add/', ThreadCreateView.as_view(), name='thread-create'),
    ]

app_name = 'forum'
