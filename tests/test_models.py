'''Tests for models'''

from datetime import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model

from user_storages.models import Storage


class StorageTestLabelMixin:
    '''Tests for label in model Storage fields'''

    def test_name_label(self):
        '''Test that the storage name label is equal to the expected label'''

        test_storage = Storage.objects.get(id=1)
        label_of_the_name_field = test_storage._meta.get_field(
            'name'
        ).verbose_name

        self.assertEqual(label_of_the_name_field, 'Название хранилища')

    def test_owner_label(self):
        '''Test that the storage owner label is equal to the expected label'''

        test_storage = Storage.objects.get(id=1)
        label_of_the_owner_field = test_storage._meta.get_field(
            'owner'
        ).verbose_name

        self.assertEqual(label_of_the_owner_field, 'Владелец хранилища')

    def test_account_login_label(self):
        '''Test that the storage account_login label is equal to the expected label'''

        test_storage = Storage.objects.get(id=1)
        label_of_the_account_login_field = test_storage._meta.get_field(
            'account_login'
        ).verbose_name

        self.assertEqual(
            label_of_the_account_login_field,
            'Логин'
        )

    def test_account_password_label(self):
        '''Test that the storage account_password label is equal to the expected label'''

        test_storage = Storage.objects.get(id=1)
        label_of_the_account_password_field = test_storage._meta.get_field(
            'account_password'
        ).verbose_name

        self.assertEqual(
            label_of_the_account_password_field,
            'Пароль'
        )

    def test_notes_label(self):
        '''Test that the storage notes label is equal to the expected label'''

        test_storage = Storage.objects.get(id=1)
        label_of_the_notes_field = test_storage._meta.get_field(
            'notes'
        ).verbose_name

        self.assertEqual(
            label_of_the_notes_field,
            'Заметки'
        )

    def test_date_of_creation_label(self):
        '''Test that the storage date_of_creation label is equal to the expected label'''

        test_storage = Storage.objects.get(id=1)
        label_of_the_date_of_creation_field = test_storage._meta.get_field(
            'date_of_creation'
        ).verbose_name

        self.assertEqual(
            label_of_the_date_of_creation_field,
            'Дата создания хранилища'
        )

    def test_date_of_edition_label(self):
        '''Test that the storage date_of_edition label is equal to the expected label'''

        test_storage = Storage.objects.get(id=1)
        label_of_the_date_of_edition_field = test_storage._meta.get_field(
            'date_of_edition'
        ).verbose_name

        self.assertEqual(
            label_of_the_date_of_edition_field,
            'Дата изменения хранилища'
        )


class StorageTestHelpTextMixin:
    '''Tests for help text in model Storage fields'''

    def test_account_login_help_text(self):
        '''Test that the storage account_login help text is equal to the expected help text'''

        test_storage = Storage.objects.get(id=1)
        help_text_of_the_account_login_field = test_storage._meta.get_field(
            'account_login'
        ).help_text

        self.assertEqual(
            help_text_of_the_account_login_field, 'Логин от аккаунта'
        )

    def test_account_password_help_text(self):
        '''Test that the storage account_password help text is equal to the expected help text'''

        test_storage = Storage.objects.get(id=1)
        help_text_of_the_account_password_field = test_storage._meta.get_field(
            'account_password'
        ).help_text

        self.assertEqual(
            help_text_of_the_account_password_field, 'Пароль от аккаунта'
        )


class StorageTestMaxLengthMixin:
    '''Tests for max length in model Storage fields'''

    def test_name_max_length(self):
        '''Test that the storage name max_length is equal to the expected max_length'''

        test_storage = Storage.objects.get(id=1)
        max_length_of_the_name_field = test_storage._meta.get_field(
            'name'
        ).max_length

        self.assertEqual(max_length_of_the_name_field, 50)

    def test_account_login_max_length(self):
        '''Test that the storage account_login max_length is equal to the expected max_length'''

        test_storage = Storage.objects.get(id=1)
        max_length_of_the_account_login_field = test_storage._meta.get_field(
            'account_login'
        ).max_length

        self.assertEqual(
            max_length_of_the_account_login_field,
            100
        )


class StorageTestUserDisplayingMixin:
    '''Tests for user displaying for model Storage'''

    def test_storage_displaying(self):
        '''Test that the storage displaying is equal to the expected displaying'''

        test_storage = Storage.objects.get(id=1)
        expected_storage_displaying = f'{test_storage.owner} - {test_storage.name}'

        self.assertEqual(expected_storage_displaying, str(test_storage))


class StorageModelTest(
        StorageTestLabelMixin, StorageTestHelpTextMixin,
        StorageTestMaxLengthMixin, StorageTestUserDisplayingMixin,
        TestCase):
    '''Tests for model Storage'''

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='test_user',
            password='test_user_password'
        )

        Storage.objects.create(
            name='TestStorage',
            owner=test_user,
            account_login='test_account_login',
            account_password='test_account_password',
            notes='',
            date_of_creation=datetime.now(),
            date_of_edition=datetime.now(),
        )
