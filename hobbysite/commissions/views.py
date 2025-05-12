from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from commissions.models import Commission, Job, JobApplication
from commissions.forms import CommissionForm
from django.db import models

class CommissionListView(ListView):
    '''
    Displays a list of all commissions, ordered by status (Open > Full > Completed > Discontinued),
    then by creation date (most recent first).
    '''
    context_object_name = "commissions"
    queryset = Commission.objects.all().order_by(
        models.Case(
            models.When(status='Open', then=0),
            models.When(status='Full', then=1),
            models.When(status='Completed', then=2),
            models.When(status='Discontinued', then=3),
            default=4,
            output_field=models.IntegerField(),
        ).desc(),  # most recent Open first
        '-created_on'
    )
    template_name = "commission_list.html"

class CommissionDetailView(DetailView):
    '''
    Displays the details of a specific commission, including its associated jobs.
    '''
    context_object_name = "commission"
    model = Commission
    extra_context = {"jobs":Job.objects.all()}
    template_name = "commission.html"

class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = "commission_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.use.profile
        return super().form_valid(form)

class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = "commission_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)

        # Auto-update commission status to Full if all jobs are full
        jobs = Job.objects.filter(commission=self.object)
        if jobs.exists() and all(job.status == 'Full' for job in jobs):
            self.object.status = 'Full'
            self.object.save()

        return response