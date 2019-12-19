"""
WSGI config for jointparty project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jointparty.settings.production')

application = get_wsgi_application()

# 20191218”jointpartyモジュールが見つからない”エラー対応
# import os

# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling

# import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectname.settings")


# application = Cling(get_wsgi_application())