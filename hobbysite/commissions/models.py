from django.db import models
from django.urls import reverse

# Create your models here.
class Commission(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def ___str___(self):
        return self.commission
    
    def get_absolute_url(self):
        return reverse('commissions:commissions-detail', args=[self.pk])