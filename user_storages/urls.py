from django.urls import path

from .views import StorageListView

app_name = 'user_storages'

urlpatterns = [
    # Index page
    path(
        '',
        StorageListView.as_view(),
        name='index'
    ),
]
