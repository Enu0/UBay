"""
WSGI config for TwoHandWebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from . import routing
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TwoHandWebsite.settings')

application = get_wsgi_application()
