from django import forms
from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'status', 'manpower_required']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['status']