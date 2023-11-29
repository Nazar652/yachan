"""
ASGI config for yachan project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from api.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yachan.settings')

django_application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_application,
    'websocket': URLRouter(websocket_urlpatterns),
    # Add other protocol routers if needed
})
