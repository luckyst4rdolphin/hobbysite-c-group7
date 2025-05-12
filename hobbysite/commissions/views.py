from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from commissions.models import Commission, Job, JobApplication
from commissions.forms import CommissionForm
from django.db import models
from django.db.models import Count, Q, Sum
from django.contrib.auth.decorators import login_required


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
        queryset = Commission.objects.annotate(
        job_total_manpower_required=Sum('job__manpower_required')).order_by(
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
        if user.is_authenticated and hasattr(user, 'profile'):
            context['my_commissions'] = Commission.objects.filter(author=user.profile)
            context['applied_commissions'] = Commission.objects.filter(
                job__jobapplication__applicant=user.profile
            ).distinct()
        else:
            context['my_commissions'] = Commission.objects.none()
            context['applied_commissions'] = Commission.objects.none()

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

        user_profile = None
        if self.request.user.is_authenticated and hasattr(self.request.user, 'profile'):
            user_profile = self.request.user.profile

        # Annotate accepted count for each job
        jobs = Job.objects.filter(commission=commission).annotate(
            accepted_count=Count('jobapplication', filter=Q(jobapplication__status='Accepted'))
        )

        job_messages = {}
        for job in jobs:
            job.open_slots = job.manpower_required - job.accepted_count
            # Default no message
            job_messages[job.pk] = ""
            if user_profile:
                # Check if user has applied
                if JobApplication.objects.filter(job=job, applicant=user_profile).exists():
                    job_messages[job.pk] = "Already applied"

        context['jobs'] = jobs
        context['job_messages'] = job_messages
        context['job_total_manpower_required'] = sum(job.manpower_required for job in jobs)
        context['job_total_open_slots'] = sum(job.open_slots for job in jobs)

        return context

class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = "commission_form.html"

    def form_valid(self, form):
        # Assign the logged-in user’s profile as the author
        form.instance.author = self.request.user.profile
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
            if jobs.exists():
                if (job.status == 'Full' for job in jobs):
                    self.object.status = 'Full'
                if job.total_manpower_required <= 0:
                    self.object.status = 'Full'
            self.object.save()

        return response

def apply_to_job(request, pk):
    print("Applying to job with ID:", pk)  # Debugging line
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to apply.")
        return redirect('login')
    job = get_object_or_404(Job, pk=pk)
    applicant = request.user.profile
    existing = JobApplication.objects.filter(job=job, applicant=applicant)
    if existing.exists():
        messages.warning(request, "You already applied to this job.")
    else:
        JobApplication.objects.create(job=job, applicant=applicant, status='Pending')
        messages.success(request, "Application submitted.")
    return redirect('commissions:commissions-detail', pk=job.commission.pk)