'''Settings for passwords_manager project'''

from os import path
from pathlib import Path

# To hide important data
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'user_storages',
    'account_management',

    # For authorization by VK network
    'social_django',

    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # For adding debug toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# For adding debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'passwords_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # For authorization by VK network
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'passwords_manager.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'TEST': {
            'NAME': 'tests_for_passwords_manager_project',
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

# Redirect url for login and logout

LOGIN_REDIRECT_URL = 'user_storages:index'

LOGOUT_REDIRECT_URL = 'account_management:login'

LOGIN_URL = 'account_management:login'

# Settings for send email messages

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_HOST_USER = config('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# For authorization by VK network

AUTHENTICATION_BACKENDS = {
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
}

SOCIAL_AUTH_VK_OAUTH2_KEY = config(
    'SOCIAL_AUTH_VK_OAUTH2_KEY'
)

SOCIAL_AUTH_VK_OAUTH2_SECRET = config(
    'SOCIAL_AUTH_VK_OAUTH2_SECRET'
)

SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

# For caching

CACHES = {
    'default': {
        # Cache will save in files in folder cache in the project
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': path.join(BASE_DIR, 'cache')
    }
}
