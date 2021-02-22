from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordChangeDoneView, PasswordResetView,
    PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import path, reverse_lazy

from .views import RegistrationView

app_name = 'account_management'

PATH_TO_PASSWORD_RESET_FOLDER = 'account_management/password_reset/'

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

    # Password reset
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name=f'{PATH_TO_PASSWORD_RESET_FOLDER}password_reset.html',
            email_template_name=f'{PATH_TO_PASSWORD_RESET_FOLDER}email_template.html',
            subject_template_name=f'{PATH_TO_PASSWORD_RESET_FOLDER}email_subject.txt',
            success_url=reverse_lazy('account_management:password_reset_done')
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name=f'{PATH_TO_PASSWORD_RESET_FOLDER}password_reset_done.html',
        ),
        name='password_reset_done'
    ),
    path(
        'password_reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name=f'{PATH_TO_PASSWORD_RESET_FOLDER}password_reset_confirm.html',
            success_url=reverse_lazy(
                'account_management:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset_complete/',
        PasswordResetCompleteView.as_view(
            template_name=f'{PATH_TO_PASSWORD_RESET_FOLDER}password_reset_complete.html',
        ),
        name='password_reset_complete'
    ),
]
