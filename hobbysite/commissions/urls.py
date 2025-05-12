from django.urls import path
from . import views
from .views import CommissionListView, CommissionDetailView, CommissionCreateView, CommissionUpdateView, JobDetailView

urlpatterns = [
    path('list/', CommissionListView.as_view(), name="commissions-list"),
    path('detail/<int:pk>', CommissionDetailView.as_view(), name="commissions-detail"),
    path('add/', CommissionCreateView.as_view(), name="commissions-create"),
    path('<int:pk>/edit/', CommissionUpdateView.as_view(), name="commissions-update"),
    path('job/<int:pk>/apply/', views.apply_to_job, name='job-apply'),
    path('job/<int:pk>/applicants/', JobDetailView.as_view(), name="job-details"),
]

app_name = "commissions"