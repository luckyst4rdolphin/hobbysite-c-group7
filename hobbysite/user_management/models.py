from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    '''
    Extends User model, accepts name and email.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('user_management:profile_page', args=[self.pk]) 