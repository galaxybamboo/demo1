"""
WSGI config for demo1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
# path = '/var/www/demo1'
# if path not in sys.path:
#     sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo1.settings")

application = get_wsgi_application()

# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()



