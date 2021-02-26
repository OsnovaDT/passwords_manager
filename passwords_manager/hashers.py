'''Hashers for password'''

from django.contrib.auth.hashers import Argon2PasswordHasher
from django.utils.crypto import get_random_string


class MoreSecureArgon2PasswordHasher(Argon2PasswordHasher):
    '''A class that is more secure than Argon2PasswordHasher'''

    time_cost = Argon2PasswordHasher.time_cost * 1_000
    parallelism = Argon2PasswordHasher.parallelism * 2

    def salt(self):
        """Generate a cryptographically secure nonce salt in ASCII with length 50"""

        return get_random_string(50)
