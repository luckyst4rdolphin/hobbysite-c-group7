from django.urls import path
from .views import MerchListView, MerchDetailView, MerchCreateView, MerchUpdateView

urlpatterns = [
    path('items/', MerchListView.as_view(), name="merch_list"),
    path('item/<int:pk>/', MerchDetailView.as_view(), name='merch_detail'),
    path('item/<int:pk>/edit', MerchUpdateView.as_view(), name='merch_update'),
    path('item/add/', MerchCreateView.as_view(), name='merch_create')
]

app_name = "merchstore"