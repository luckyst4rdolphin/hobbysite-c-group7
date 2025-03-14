from django.views.generic import ListView, DetailView
from commissions.models import Commission, Comment

class CommissionListView(ListView):
    '''
    Displays a list of all commissions, ordered by their creation date in ascending order.
    '''
    context_object_name = "commissions"
    queryset = Commission.objects.all().order_by('created_on')
    template_name = "commission_list.html"

class CommissionDetailView(DetailView):
    '''
    Displays the details of a specific commission, including its associated comments.

    The comments are filtered to only include those belonging to the commission being viewed 
    and are displayed in descending order based on their creation date (newest first).'
    '''
    context_object_name = "commission"
    model = Commission
    extra_context = {"comments":Comment.objects.all()}
    template_name = "commission.html"
