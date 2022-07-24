from .base import *

""" Override base settings so it suits production environment """

DOTENV_FILE = os.path.join(BASE_DIR.parent, '.env.prod')

env.read_env(DOTENV_FILE)
config = Config(RepositoryEnv(DOTENV_FILE))


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

SHOPIFY__ACCESS_TOKEN = config('SHOPIFY__ACCESS_TOKEN')
SHOPIFY_STORE_URL = config('SHOPIFY_STORE_URL')

DATABASES['default']['NAME'] = config('DATABASE_NAME')
DATABASES['default']['HOST'] = config('DATABASE_HOST')
DATABASES['default']['PORT'] = config('DATABASE_PORT')
DATABASES['default']['USER'] = config('DATABASE_USER')
DATABASES['default']['PASSWORD'] = config('DATABASE_PASSWORD')

SESSION_COOKIE_SECURE = True
CSRF_COQKIE_SECURE = True
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000 # 1 year 
SECURE_HSTS_PRELOAD = True 
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SHOPIFY__ACCESS_TOKEN = config('SHOPIFY_ACCESS_TOKEN')
SHOPIFY_STORE_URL = config('SHOPIFY_STORE_URL')
SHOPIFY_API_VERSION = config('SHOPIFY_API_VERSION')