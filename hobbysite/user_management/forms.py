from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    '''
    Form for creating new user.
    Has the fields username, name, email, and password.
    '''
    username = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                           'class': 'form-control',
                                                           }))
    name = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                           'class': 'form-control',
                                                           }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    class Meta:
        model = User
        fields = ["username", "name", "email", "password1"]

class ProfileForm(forms.ModelForm):
    '''
    Form for creating new profile for a user.
    Has the fields name and email.
    '''
    class Meta:
        model = Profile
        fields = ["name", "email"]