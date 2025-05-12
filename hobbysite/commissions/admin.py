from django.contrib import admin
from .models import Commission, Job, JobApplication

class CommissionAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the Commission model.
    '''
    model = Commission
    list_display = ('title', 'status', 'created_on', 'updated_on')
    list_filter = ('status',)
    search_fields = ('title', 'description')

class JobAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the Job model.
    '''
    model = Job
    list_display = ('commission', 'role', 'manpower_required', 'status')
    list_filter = ('status', 'commission')
    search_fields = ('role',)

class JobApplicationAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the JobApplication model.
    '''
    model = JobApplication
    list_display = ('job', 'applicant', 'status', 'applied_on')
    list_filter = ('status', 'job')
    search_fields = ('applicant__user__username',)

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
