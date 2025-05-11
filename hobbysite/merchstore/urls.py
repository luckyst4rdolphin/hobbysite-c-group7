from django.urls import path
from .views import MerchListView, MerchDetailView, MerchCreateView

urlpatterns = [
    path('items/', MerchListView.as_view(), name="merch_list"),
    path('item/<int:pk>/', MerchDetailView.as_view(), name='merch_detail'),
    path('item/add/', MerchCreateView.as_view(), name='merch_create')
]

app_name = "merchstore"