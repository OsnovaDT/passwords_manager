from django.urls import path

from .views import StorageListView, StorageCreateView

app_name = 'user_storages'

urlpatterns = [
    # Index page
    path(
        '',
        StorageListView.as_view(),
        name='index'
    ),

    # Create storage page
    path(
        'create_storage/',
        StorageCreateView.as_view(),
        name='create_storage'
    ),
]
