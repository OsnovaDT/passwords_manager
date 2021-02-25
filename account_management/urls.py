'''Urls for account_management app'''

from django.contrib.auth.views import (
    # Login and logout import
    LoginView, LogoutView,

    # Password change import
    PasswordChangeView, PasswordChangeDoneView,

    # Password reset import
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls import path, reverse_lazy, include

from account_management.views import RegistrationView

app_name = 'account_management'  # pylint: disable=invalid-name

PATH_TO_PASSWORD_RESET_FOLDER = 'account_management/password_reset/'

urlpatterns = [
    # Login
    path(
        'login/',
        LoginView.as_view(
            template_name='account_management/login.html'
        ),
        name='login'
    ),

    # Logout
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    # Change password

    # Page with info that password successfully changed
    path(
        'change_password/done/',
        PasswordChangeDoneView.as_view(
            template_name='account_management/change_password_done.html'
        ),
        name='change_password_done'
    ),

    # Page with form to change password
    path(
        'change_password/',
        PasswordChangeView.as_view(
            template_name='account_management/change_password.html',

            # After password will be changed we'll go to the change password done page
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

    # Page with info that message sent to user email
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name=PATH_TO_PASSWORD_RESET_FOLDER + 'password_reset_done.html',
        ),
        name='password_reset_done'
    ),

    # Page where user enter a new password
    path(
        'password_reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name=PATH_TO_PASSWORD_RESET_FOLDER + 'password_reset_confirm.html',

            # After password will be reset we'll go to the password reset complete page
            success_url=reverse_lazy(
                'account_management:password_reset_complete'
            )
        ),
        name='password_reset_confirm'
    ),

    # Page with info that password successfully reset
    path(
        'password_reset_complete/',
        PasswordResetCompleteView.as_view(
            template_name=PATH_TO_PASSWORD_RESET_FOLDER + 'password_reset_complete.html',
        ),
        name='password_reset_complete'
    ),

    # Page with form to send message to user email for reset password
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name=PATH_TO_PASSWORD_RESET_FOLDER + 'password_reset.html',

            # Subject for message that we'll send to the user
            subject_template_name=PATH_TO_PASSWORD_RESET_FOLDER + 'email_subject.txt',

            # Text for message that we'll send to the user
            email_template_name=PATH_TO_PASSWORD_RESET_FOLDER + 'email_template.html',

            # After message will send to user email we'll go to the password reset done page
            success_url=reverse_lazy('account_management:password_reset_done')
        ),
        name='password_reset'
    ),

    # Authorization by VK network
    path(
        'social/',
        include('social_django.urls', namespace='social')
    ),

]
