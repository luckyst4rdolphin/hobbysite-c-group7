from django.db import models
from django.urls import reverse
from user_management.models import Profile

class Commission(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Full', 'Full'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            models.Case(
                models.When(status='Open', then=0),
                models.When(status='Full', then=1),
                models.When(status='Completed', then=2),
                models.When(status='Discontinued', then=3),
                default=4,
                output_field=models.IntegerField(),
            ),
            'created_on'
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commissions-detail', args=[self.pk])
    
class Job(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Full', 'Full'),
    ]
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE
    )
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveBigIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )

    class Meta:
        ordering = [
            models.Case(
                models.When(status='Open', then=0),
                models.When(status='Full', then=1),
                default=2,
                output_field=models.IntegerField(),
            ),
            '-manpower_required',
            'role'
        ]

    def __str__(self):
        return f"{self.role} - {self.status}"

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    applicant = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            models.Case(
                models.When(status='Pending', then=0),
                models.When(status='Accepted', then=1),
                models.When(status='Rejected', then=2),
                default=3,
                output_field=models.IntegerField(),
            ),
            '-applied_on'
        ]

    def __str__(self):
        return f"{self.applicant.name} - {self.job.role} - {self.status}"