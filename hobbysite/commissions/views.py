from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from commissions.models import Commission, Job
from commissions.forms import CommissionForm
from django.db import models

class CommissionListView(ListView):
    '''
    Displays a list of all commissions, ordered by status (Open > Full > Completed > Discontinued),
    then by creation date (most recent first).
    '''
    model = Commission
    template_name = "commission_list.html"
    context_object_name = "commissions"
    # Sorting commissions by status and creation date
    def get_queryset(self):
        queryset = Commission.objects.all().order_by(
            models.Case(
                models.When(status='Open', then=0),
                models.When(status='Full', then=1),
                models.When(status='Completed', then=2),
                models.When(status='Discontinued', then=3),
                default=4,
                output_field=models.IntegerField(),
            ).desc(),  # Sorting statuses first (Open > Full > Completed > Discontinued)
            '-created_on'  # Sorting by created_on in descending order (most recent first)
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # If the user is logged in, add two categories above the list:
        if user.is_authenticated:
            # Get commissions created by the logged-in user
            my_commissions = Commission.objects.filter(author=user)
            
            # Get commissions the user has applied to
            applied_commissions = Commission.objects.filter(job__jobapplication__applicant=user)

            context['my_commissions'] = my_commissions
            context['applied_commissions'] = applied_commissions

        return context

class CommissionDetailView(DetailView):
    '''
    Displays the details of a specific commission, including its associated jobs.
    '''
    model = Commission
    context_object_name = "commission"
    template_name = "commission.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filter jobs by the current commission
        commission = self.object
        context['jobs'] = Job.objects.filter(commission=commission)
        return context

class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = "commission_form.html"

    def form_valid(self, form):
        # Assign the logged-in user’s profile as the author
        form.instance.author = self.request.use.profile
        return super().form_valid(form)

class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = "commission_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)

        # Only update to 'Full' if the commission is currently 'Open'
        if self.object.status == 'Open':
            jobs = Job.objects.filter(commission=self.object)
            if jobs.exists() and all(job.status == 'Full' for job in jobs):
                self.object.status = 'Full'
                self.object.save()

        return response