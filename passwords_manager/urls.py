'''Urls for passwords_manager project'''

from django.contrib import admin
from django.urls import path, include
from debug_toolbar import urls as debug_toolbar_urls

urlpatterns = [
    # Administrative site
    path('admin/', admin.site.urls),

    # Index page
    path('index/', include('user_storages.urls')),

    # Account management
    path('account/', include('account_management.urls')),

    # For authorization by VK network
    path(
        'social/',
        include('social_django.urls', namespace='social')
    ),

    # For adding debug toolbar
    path(
        '__debug__/',
        include(debug_toolbar_urls)
    ),
]
