from pathlib import Path
import os
import environ
from decouple import config, Config, RepositoryEnv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
ALLOWED_HOSTS = ['*']

# Application definition

# APPS == components
INSTALLED_APPS = [
    'admin_override',
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'polymorphic',

    'wagmin',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',
    'wagtail.contrib.styleguide',
    'wagtail.contrib.modeladmin',
    'wagtailfontawesome',
    
    'taggit',
    'modelcluster',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'cloudinary_storage',
    'cloudinary',
    'problems',
    'skripte',
    'mature',
    'media',
    'shopify_models',
    'cheatsheets',
    'adminsortable2',
    'rest_framework',
    'api',
    'frontend',
    # 'courses',
    'course',
    "corsheaders",
    'dbbackup',  # django-dbbackup
    'django_extensions',
    'ckeditor',
    'ckeditor_uploader',

    # 'merged_inlines',
]

WAGTAIL_SITE_NAME = 'Wagtail admin'

X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': Path(BASE_DIR / 'backups') }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'gradmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'gradmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gradmin',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = config('STATIC_ROOT', cast=str)

STATICFILES_DIRS = [
    # BASE_DIR / "static",
    BASE_DIR / 'frontend/static',
]

DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = Path(BASE_DIR / 'problems' / 'static' / 'problems' / 'images')
# MEDIA_URL = str('/problems/static/problems/images/')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
        'extraPlugins': 'codesnippet',
    },
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:80",
    'https://localhost:8000',
    'https://theehhdude23.eu.pythonanywhere.com',
    'https://gradivo.hr',
    'https://msandalj23.myshopify.com',
    'https://gradivo-hr23.myshopify.com'
]

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }



TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

DATA_UPLOAD_MAX_NUMBER_FIELDS = None
WAGTAILADMIN_BASE_URL = '/cms'

# SHOPIFY
SHOPIFY_ACCESS_TOKEN = config('SHOPIFY_ACCESS_TOKEN')
SHOPIFY_STORE_URL = config('SHOPIFY_STORE_URL')
SHOPIFY_API_VERSION = config('SHOPIFY_API_VERSION')

# CLOUDINARY
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}

# VIMEO
VIMEO_TOKEN = config('VIMEO_TOKEN')
VIMEO_KEY = config('VIMEO_KEY')
VIMEO_SECRET = config('VIMEO_SECRET')

# MATHPIX
MATHPIX_APP_ID = config('MATHPIX_APP_ID')
MATHPIX_APP_KEY = config('MATHPIX_APP_KEY')