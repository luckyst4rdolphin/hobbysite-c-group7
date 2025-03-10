from django.urls import path
from .views import products, product

urlpatterns = [
    path('merchstore/items/', products, name = "merch_store"),
    path('merchstore/item/<int:pk>/', product, name = "merch_detail")
]

app_name = 'merchstore'