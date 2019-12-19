from .base import *
import os
import environ

BASE_DIR = environ.Path(__file__) - 3

env = environ.Env()

# 環境変数でDJANGO_READ_ENV_FILEをTrueにしておくと.envを読んでくれる。
READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE', default=True)
if READ_ENV_FILE:
    env_file = str(BASE_DIR.path('.env.prod'))
    env.read_env(env_file)

SECRET_KEY = "=llv2rzj$^vk)wx7n_u9v$o(ic2i-7w)m&0il3vlamiei2#&d6"
ALLOWED_HOSTS = []
DEBUG = False

# 一旦コメントアウト、後ほど20191219

# SECRET_KEY = os.environ.get("SECRET_KEY")
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS") #.split(" ")
# DEBUG = 0

# DATABASES = {
#     'default': env.prod.db()
# }

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE','django.db.backends.postgresql'),
        'NAME': os.environ.get('DATABASE_DB', os.path.join(BASE_DIR, 'db.postgresql')),
        'USER': os.environ.get('DATABASE_USER', 'user'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'password'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}

WSGI_APPLICATION = 'jointparty.wsgi.application'