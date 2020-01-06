from .base import *
import os
import environ

BASE_DIR = environ.Path(__file__) - 3
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

env = environ.Env()

# 環境変数でDJANGO_READ_ENV_FILEをTrueにしておくと.envを読んでくれる。
READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE', default=False)
if READ_ENV_FILE:
    env_file = str(BASE_DIR.path('.env'))
    env.read_env(env_file)
 
DEBUG = int(os.environ.get("DEBUG"))

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

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

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(ROOT_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')

# デバッグツール（django-debug-toolbar）の設定
# 下記とりあえず毎回確認して変える ↓REMOTE_ADDRのIP（buildしたらIPが変わる為）
INTERNAL_IPS = ('127.0.0.1', '172.18.0.1')
MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'debug_toolbar',
)
# 表示する内容
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}