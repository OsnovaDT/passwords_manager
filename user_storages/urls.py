from django.urls import path

from .views import (
    StorageListView, StorageCreateView,
    StorageUpdateView, StorageDeleteView,
    SearchStorageView
)

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

    # Update storage page
    path(
        'update_storage/<int:pk>/',
        StorageUpdateView.as_view(),
        name='update_storage'
    ),

    # Delete storage page
    path(
        'delete_storage/<int:pk>/',
        StorageDeleteView.as_view(),
        name='delete_storage'
    ),

    # Delete storage page
    path(
        'search_storage/',
        SearchStorageView.as_view(),
        name='search_storage'
    ),
]
