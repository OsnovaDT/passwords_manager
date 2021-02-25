'''Forms for user_storages app'''

from django import forms

from user_storages.models import Storage


class StorageUpdateForm(forms.ModelForm):
    '''Storage updating form'''

    class Meta:  # pylint: disable=too-few-public-methods
        '''Meta for Storage updating form'''

        fields = (
            'name', 'account_login',
            'account_password', 'notes',
        )
        model = Storage


class StorageCreateForm(forms.ModelForm):
    '''Storage creation form'''

    class Meta:  # pylint: disable=too-few-public-methods
        '''Meta for Storage creation form'''

        fields = (
            'name', 'account_login',
            'account_password', 'notes',
        )
        model = Storage

        # Account_password will look like dots
        widgets = {
            'account_password': forms.PasswordInput(),
        }
