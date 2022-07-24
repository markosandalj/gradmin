from .base import *

""" Override base settings so it suits development environment """
DOTENV_FILE = os.path.join(BASE_DIR.parent, '.env.dev')

env.read_env(DOTENV_FILE)
config = Config(RepositoryEnv(DOTENV_FILE))


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware', 
]

DATABASES['default']['NAME'] = config('DATABASE_NAME')
DATABASES['default']['HOST'] = config('DATABASE_HOST')
DATABASES['default']['PORT'] = config('DATABASE_PORT')
DATABASES['default']['USER'] = config('DATABASE_USER')
DATABASES['default']['PASSWORD'] = config('DATABASE_PASSWORD')

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")

SHOPIFY__ACCESS_TOKEN = config('SHOPIFY_ACCESS_TOKEN')
SHOPIFY_STORE_URL = config('SHOPIFY_STORE_URL')
SHOPIFY_API_VERSION = config('SHOPIFY_API_VERSION')