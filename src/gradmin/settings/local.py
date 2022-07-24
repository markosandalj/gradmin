from .base import *

""" Override base settings so it suits local environment """

DOTENV_FILE = os.path.join(BASE_DIR.parent, '.env.local')

env.read_env(DOTENV_FILE)
config = Config(RepositoryEnv(DOTENV_FILE))


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

STATIC_ROOT = config('STATIC_ROOT')

DATABASES['default']['NAME'] = config('DATABASE_NAME', cast=str)
DATABASES['default']['HOST'] = config('DATABASE_HOST', cast=str)
DATABASES['default']['PORT'] = config('DATABASE_PORT', cast=str)
DATABASES['default']['USER'] = config('DATABASE_USER', cast=str)
DATABASES['default']['PASSWORD'] = config('DATABASE_PASSWORD', cast=str)

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware', 
]

SHOPIFY__ACCESS_TOKEN = config('SHOPIFY_ACCESS_TOKEN')
SHOPIFY_STORE_URL = config('SHOPIFY_STORE_URL')
SHOPIFY_API_VERSION = config('SHOPIFY_API_VERSION')