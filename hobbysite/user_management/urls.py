from django.urls import path
from user_management.views import UserCreateView, ProfileEdit

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register_user'),
    path('profile/', ProfileEdit.as_view(), name='profile_edit'),
    ]

app_name = 'user_management'