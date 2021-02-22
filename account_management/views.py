from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm


class RegistrationView(CreateView):
    template_name = 'account_management/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user_storages:index')
