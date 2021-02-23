from django.db import models
from django.core import validators


class Storage(models.Model):
    name = models.CharField(
        'Название хранилища',
        max_length=50,
        db_index=True,
        db_column='name'
    )

    owner = models.ForeignKey(
        'auth.User',
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

    account_password = models.CharField(
        'Пароль',
        max_length=50,
        db_column='account_password',
        help_text='Пароль от аккаунта',
    )

    notes = models.TextField(
        'Заметки',
        null=True,
        blank=True,
        db_column='notes'
    )

    date_of_creation = models.DateField(
        'Дата создания хранилища',
        auto_now_add=True,
        db_column='date_of_creation'
    )

    date_of_edition = models.DateField(
        'Дата изменения хранилища',
        auto_now=True,
        db_column='date_of_edition'
    )

    def __str__(self):
        return f'{self.owner} - {self.name}'

    class Meta:
        verbose_name = 'Хранилище'
        verbose_name_plural = 'Хранилища'
        ordering = ['date_of_edition', 'name']
        unique_together = ('name', 'owner')
        db_table = 'storage'
