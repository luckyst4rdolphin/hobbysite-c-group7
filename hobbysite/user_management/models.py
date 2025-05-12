from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    '''
    Extends User model, accepts name and email.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        '''
        Returns the user's name.
        '''
        return self.name