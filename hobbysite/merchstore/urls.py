from django.urls import path
from .views import MerchListView, MerchDetailView, MerchCreateView, MerchUpdateView, MerchCartView, MerchTransactionView

urlpatterns = [
    path('items/', MerchListView.as_view(), name="merch_list"),
    path('item/<int:pk>/', MerchDetailView.as_view(), name='merch_detail'),
    path('item/<int:pk>/edit', MerchUpdateView.as_view(), name='merch_update'),
    path('item/add/', MerchCreateView.as_view(), name='merch_create'),
    path('cart/', MerchCartView.as_view(), name='merch_cart'),
    path('transactions/', MerchTransactionView.as_view(), name='merch_transaction')
]

app_name = "merchstore"