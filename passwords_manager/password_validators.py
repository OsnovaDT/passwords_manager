'''My password validators'''


from django.core.exceptions import ValidationError
from django.utils.translation import gettext


class AtLeast1NumberValidator:
    '''Validator that check that password has at least 1 number'''

    def __init__(self):
        pass

    @staticmethod
    def validate(password, user=None):
        '''Validate that password has at least 1 number'''

        if str(password).isalpha():
            raise ValidationError(
                gettext("Ваш пароль должен содержать хотя бы 1 цифру"),
                code='password_is_alpha',
            )

    @staticmethod
    def get_help_text():
        '''Send help text to user that explain him why his password is wrong'''

        return gettext(
            "Ваш пароль должен содержать хотя бы 1 цифру"
        )


class AtLeast1LowercaseLetterValidator:
    '''Validator that check that password has at least 1 lowercase letter'''

    def __init__(self):
        pass

    @staticmethod
    def validate(password, user=None):
        '''Validate that password has at least 1 lowercase letter'''

        if str(password).isupper():
            raise ValidationError(
                gettext(
                    "Ваш пароль должен содержать хотя бы 1 букву нижнего регистра"),
                code='password_is_lower',
            )

    @staticmethod
    def get_help_text():
        '''Send help text to user that explain him why his password is wrong'''

        return gettext(
            "Ваш пароль должен содержать хотя бы 1 букву нижнего регистра. Например: а, б, ф"
        )


class AtLeast1UppercaseLetterValidator:
    '''Validator that check that password has at least 1 uppercase letter'''

    def __init__(self):
        pass

    @staticmethod
    def validate(password, user=None):
        '''Validate that password has at least 1 uppercase letter'''

        if str(password).islower():
            raise ValidationError(
                gettext(
                    "Ваш пароль должен содержать хотя бы 1 букву верхнего регистра"),
                code='password_is_upper',
            )

    @staticmethod
    def get_help_text():
        '''Send help text to user that explain him why his password is wrong'''

        return gettext(
            "Ваш пароль должен содержать хотя бы 1 букву нижнего регистра. Например: А, Б, Ф"
        )
