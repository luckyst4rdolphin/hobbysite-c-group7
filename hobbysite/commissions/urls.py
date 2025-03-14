from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('commissions/list/', CommissionListView.as_view(), name="commissions-list"),
    path('commissions/detail/<int:pk>', CommissionDetailView.as_view(), name="commissions-detail"),
]

app_name = "commissions"