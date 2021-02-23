from django import forms

from .models import Storage


class StorageCreateForm(forms.ModelForm):
    class Meta:
        fields = (
            'name', 'account_login',
            'account_password', 'notes',
        )
        model = Storage
        widgets = {
            'account_password': forms.PasswordInput(),
        }


class StorageForm(forms.ModelForm):
    class Meta:
        fields = (
            'name', 'account_login',
            'account_password', 'notes',
        )
        model = Storage
