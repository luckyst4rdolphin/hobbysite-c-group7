from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from .models import Profile
from .forms import RegisterForm, ProfileForm
from django.urls import reverse_lazy

class UserCreateView(CreateView):
    template_name = "./registration/register.html"
    form_class = RegisterForm
    success_url = '/accounts/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        Profile.objects.create(user=user, name=form.cleaned_data['name'], email=form.cleaned_data['email'])
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = context['form']
        return context

class ProfileEdit(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "./profile.html"
    success_url = reverse_lazy('user_management:update_profile')

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.object
        context['profile'] = context['form']
        return context