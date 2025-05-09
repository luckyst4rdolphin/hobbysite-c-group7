from django.urls import path
from user_management.views import UserCreateView, ProfileEdit, ProfilePage

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register_user'),
    path('profile_form/', ProfileEdit.as_view(), name='profile_edit'),
    path('profile/', ProfilePage.as_view(), name='profile_page'),
    ]

app_name = 'user_management'