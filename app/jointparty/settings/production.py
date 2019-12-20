from .base import *
import os
import environ

BASE_DIR = environ.Path(__file__) - 3

env = environ.Env()

# 環境変数でDJANGO_READ_ENV_FILEをTrueにしておくと.envを読んでくれる。
READ_ENV_FILE = True # env.bool('DJANGO_READ_ENV_FILE', default=True)
if READ_ENV_FILE:
    env_file = str(BASE_DIR.path('.env.prod'))
    env.read_env(env_file)

SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
DEBUG = int(os.environ.get("DEBUG"))

# GKE_DEPLOY = env.bool('GKE_DEPLOY', default=False)
# if GKE_DEPLOY:
#     DATABASES = {
#         'default': {
#             'ENGINE': os.environ.get('DATABASE_ENGINE','django.db.backends.postgresql'),
#             'NAME': os.environ.get('DATABASE_DB', os.path.join(BASE_DIR, 'db.postgresql')),
#             'USER': os.environ.get('DATABASE_USER', 'user'),
#             'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'password'),
#             'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
#             'PORT': os.environ.get('DATABASE_PORT', '5432'),
#         }
#     }
# else:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '/cloudsql/jointparty-sql',
        'NAME': 'polls',
        'USER': 'admin',
        'PASSWORD': 'horikoudai',
    }
}


WSGI_APPLICATION = 'jointparty.wsgi.application'