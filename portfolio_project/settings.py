import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'django-insecure-jarvis-lameck-portfolio-secret-key-change-in-prod'
)

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

def comma_separated_env(name):
    """Return non-empty, comma-separated environment values."""
    return [value.strip() for value in os.environ.get(name, '').split(',') if value.strip()]


# Keep Render and local hosts allowed even when the dashboard adds a custom
# domain through ALLOWED_HOSTS.
ALLOWED_HOSTS = [
    '*',
    'localhost',
    '127.0.0.1',
    'jarvislameck.online',
    'www.jarvislameck.online',
]
render_hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME', '').strip()
if render_hostname:
    ALLOWED_HOSTS.append(render_hostname)
for host in comma_separated_env('ALLOWED_HOSTS'):
    ALLOWED_HOSTS.append(host.replace('https://', '').replace('http://', '').rstrip('/'))
ALLOWED_HOSTS = list(dict.fromkeys(ALLOWED_HOSTS))

# Django requires a scheme here. Accept a full origin or a bare domain typed
# in Render, such as jarvislameck.online.
CSRF_TRUSTED_ORIGINS = []
for origin in comma_separated_env('CSRF_TRUSTED_ORIGINS') or ['https://jarvislameck.online']:
    CSRF_TRUSTED_ORIGINS.append(
        origin if origin.startswith(('http://', 'https://')) else f'https://{origin}'
    )
WHITENOISE_MANIFEST_STRICT = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'portfolio_app', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_project.wsgi.application'

database_url = os.environ.get('DATABASE_URL', '').strip()

if database_url:
    try:
        import dj_database_url

        DATABASES = {
            'default': dj_database_url.parse(
                database_url,
                conn_max_age=600,
                conn_health_checks=True,
            ),
        }
    except Exception:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
