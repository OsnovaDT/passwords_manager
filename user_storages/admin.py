from django.contrib import admin

from .models import Storage


class StorageAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'owner', 'account_login',
        'account_password', 'notes',
        'date_of_creation', 'date_of_edition',
    )

    list_display_links = ('name', 'owner',)

    search_fields = ('name', 'owner',)


admin.site.register(Storage, StorageAdmin)
