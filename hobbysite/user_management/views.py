from django.views.generic import CreateView
from .models import Profile
from .forms import RegisterForm

class UserCreateView(CreateView):
    model = Profile
    template_name = "./registration/register.html"
    form_class = RegisterForm
    success_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['register_form'] = context['form']
        return context
