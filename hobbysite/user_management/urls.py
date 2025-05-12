from django.urls import path
from user_management.views import UserCreateView, ProfileEdit
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register_user'),
    path('profile/', ProfileEdit.as_view(), name='update_profile'),
    ]

app_name = 'user_management'