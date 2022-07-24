from .base import *

""" Override base settings so it suits production environment """

DOTENV_FILE = os.path.join(BASE_DIR.parent, '.env.prod')

env.read_env(DOTENV_FILE)
config = Config(RepositoryEnv(DOTENV_FILE))


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

STATIC_ROOT = config('STATIC_ROOT', cast=str)

DATABASES['default']['NAME'] = config('DATABASE_NAME', cast=str)
DATABASES['default']['HOST'] = config('DATABASE_HOST', cast=str)
DATABASES['default']['PORT'] = config('DATABASE_PORT', cast=str)
DATABASES['default']['USER'] = config('DATABASE_USER', cast=str)
DATABASES['default']['PASSWORD'] = config('DATABASE_PASSWORD', cast=str)

SESSION_COOKIE_SECURE = True
CSRF_COQKIE_SECURE = True
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000 # 1 year 
SECURE_HSTS_PRELOAD = True 
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SHOPIFY_ACCESS_TOKEN = config('SHOPIFY_ACCESS_TOKEN')
SHOPIFY_STORE_URL = config('SHOPIFY_STORE_URL')
SHOPIFY_API_VERSION = config('SHOPIFY_API_VERSION')

# CLOUDINARY
CLOUDINARY_STORAGE['CLOUD_NAME'] = config('CLOUDINARY_CLOUD_NAME')
CLOUDINARY_STORAGE['API_KEY'] = config('CLOUDINARY_API_KEY')
CLOUDINARY_STORAGE['API_SECRET'] = config('CLOUDINARY_API_SECRET')

# VIMEO
VIMEO_TOKEN = config('VIMEO_TOKEN')
VIMEO_KEY = config('VIMEO_KEY')
VIMEO_SECRET = config('VIMEO_SECRET')

# MATHPIX
MATHPIX_APP_ID = config('MATHPIX_APP_ID')
MATHPIX_APP_KEY = config('MATHPIX_APP_KEY')