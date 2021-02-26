'''Tests for forms'''

from django.test import TestCase

from account_management.forms import RegistrationForm
from user_storages.forms import StorageUpdateForm, StorageCreateForm


class RegistrationFormTest(TestCase):
    '''Tests for form RegistrationForm'''

    def test_form_fields_amount(self):
        '''Test that form fields amount is equal to expected amount'''

        form = RegistrationForm()
        expected_form_fields_amount = 4
        self.assertEqual(len(form.fields), expected_form_fields_amount)

    def test_form_fields_order(self):
        '''Test that form fields order is equal to expected order'''

        form = RegistrationForm()
        expected_form_fields_order = (
            'username', 'email',
            'password1', 'password2'
        )
        form_fields_order = tuple(form.fields.keys())
        self.assertEqual(form_fields_order, expected_form_fields_order)


class StorageUpdateFormTest(TestCase):
    '''Tests for form StorageUpdateForm'''

    def test_form_fields_amount(self):
        '''Test that form fields amount is equal to expected amount'''

        form = StorageUpdateForm()
        expected_form_fields_amount = 4
        self.assertEqual(len(form.fields), expected_form_fields_amount)

    def test_form_fields_order(self):
        '''Test that form fields order is equal to expected order'''

        form = StorageUpdateForm()
        expected_form_fields_order = (
            'name', 'account_login',
            'account_password', 'notes',
        )
        form_fields_order = tuple(form.fields.keys())
        self.assertEqual(form_fields_order, expected_form_fields_order)


class StorageCreateFormTest(TestCase):
    '''Tests for form StorageCreateForm'''

    def test_form_fields_amount(self):
        '''Test that form fields amount is equal to expected amount'''

        form = StorageCreateForm()
        expected_form_fields_amount = 4
        self.assertEqual(len(form.fields), expected_form_fields_amount)

    def test_form_fields_order(self):
        '''Test that form fields order is equal to expected order'''

        form = StorageCreateForm()
        expected_form_fields_order = (
            'name', 'account_login',
            'account_password', 'notes',
        )
        form_fields_order = tuple(form.fields.keys())
        self.assertEqual(form_fields_order, expected_form_fields_order)
