from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordChangeDoneView
)
from django.urls import path, reverse_lazy

from .views import RegistrationView

app_name = 'account_management'

urlpatterns = [
    # Login
    path(
        'login/',
        LoginView.as_view(template_name='account_management/login.html'),
        name='login'
    ),

    # Logout
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    # Change password
    path(
        'change_password/done/',
        PasswordChangeDoneView.as_view(
            template_name='account_management/change_password_done.html'
        ),
        name='change_password_done'
    ),

    path(
        'change_password/',
        PasswordChangeView.as_view(
            template_name='account_management/change_password.html',
            success_url=reverse_lazy(
                'account_management:change_password_done'
            ),
        ),
        name='change_password'
    ),

    # Registration
    path(
        'registration/',
        RegistrationView.as_view(),
        name='registration'
    ),
]
