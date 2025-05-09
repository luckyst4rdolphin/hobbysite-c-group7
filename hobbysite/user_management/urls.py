from django.urls import path
from user_management.views import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register_user'),
    ]

app_name = 'user_management'