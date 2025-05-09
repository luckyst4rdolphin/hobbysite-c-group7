from django.views.generic import CreateView
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
    
class  ProfileEdit(CreateView):
    model = Profile
    template_name = "./profile_form.html"
    form_class = ProfileForm
    success_url = '/home/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProfileEdit, self).get_context_data(**kwargs)
        context['profile_form'] = context['form']
        return context
