'''Forms for account_management app'''

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    '''Form for new user registration'''

    # Add new field to the form
    email = forms.EmailField()

    class Meta:  # pylint: disable=too-few-public-methods
        '''Meta for registration form'''

        fields = (
            'username', 'email',

            # Password and confirm password
            'password1', 'password2',
        )

        # User model
        model = get_user_model()
