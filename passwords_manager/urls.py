from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('user_storages.urls')),
    path('account/', include('account_management.urls')),

    # VK authorization
    path(
        'social/',
        include('social_django.urls', namespace='social')
    ),

    # Debug toolbar
    path(
        '__debug__/',
        include(debug_toolbar.urls)
    ),
]
