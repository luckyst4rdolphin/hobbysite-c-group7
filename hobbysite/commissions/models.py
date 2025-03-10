from django.db import models

# Create your models here.
class Commission(models.Model):

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    description = models.TextField()
    people_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

class Comment(models.Model):
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]