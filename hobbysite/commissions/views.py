from django.views.generic import ListView, DetailView
from commissions.models import Commission, Comment

class CommissionListView(ListView):
    context_object_name = "commissions"
    queryset = Comment.objects.all().order_by('created_on')
    template_name = "commission_list.html"

class CommissionDetailView(DetailView):
    context_object_name = "commission"
    model = Comment
    template_name = "commission.html"
