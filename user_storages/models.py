'''Models for user_storages app'''

from django.db import models
# To encrypt field account_password
from pgcrypto import EncryptedCharField


class Storage(models.Model):
    '''User storage model'''

    name = models.CharField(
        'Название хранилища',
        max_length=50,
        db_index=True,
        db_column='name'
    )

    owner = models.ForeignKey(
        # Choose user from users that there are on the site
        'auth.User',

        # If we'll delete the owner all his storages will delete too
        on_delete=models.CASCADE,
        verbose_name='Владелец хранилища',
        db_column='owner',
    )

    account_login = models.CharField(
        'Логин',
        max_length=100,
        db_column='account_login',
        help_text='Логин от аккаунта'
    )

    account_password = EncryptedCharField(
        'Пароль',
        max_length=50,
        db_column='account_password',
        help_text='Пароль от аккаунта',
    )

    notes = models.TextField(
        'Заметки',

        # This field can be empty
        null=True, blank=True,
        db_column='notes'
    )

    date_of_creation = models.DateField(
        'Дата создания хранилища',

        # This field won't be change when user will change his storage
        auto_now_add=True,
        db_column='date_of_creation'
    )

    date_of_edition = models.DateTimeField(
        'Дата изменения хранилища',

        # This field will change when user will change his storage
        auto_now=True,
        db_column='date_of_edition'
    )

    def __str__(self):
        return f'{self.owner} - {self.name}'

    class Meta:  # pylint: disable=too-few-public-methods
        '''Meta for user storage model'''

        verbose_name = 'Хранилище'
        verbose_name_plural = 'Хранилища'
        ordering = ['-date_of_edition', 'name']
        unique_together = ('name', 'owner')
        db_table = 'storage'
