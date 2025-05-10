from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Profile
from .forms import RegisterForm, ProfileForm
from django.urls import reverse_lazy

class UserCreateView(CreateView):
    template_name = "./registration/register.html"
    form_class = RegisterForm
    success_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['register_form'] = context['form']
        return context
    
class  ProfileEdit(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "./profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProfileEdit, self).get_context_data(**kwargs)
        context['profile_form'] = context['form']
        return context
