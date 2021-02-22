from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'account_management'

urlpatterns = [
    # Login
    path(
        'login/',
        LoginView.as_view(template_name='account_management/login.html'),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
]
