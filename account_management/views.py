'''Views for account_management app'''

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from account_management.forms import RegistrationForm


class RegistrationView(CreateView):  # pylint: disable=too-many-ancestors
    '''View for new user registration'''

    form_class = RegistrationForm

    template_name = 'account_management/registration.html'

    # After form execution we'll go to the login page
    success_url = reverse_lazy('account_management:login')
