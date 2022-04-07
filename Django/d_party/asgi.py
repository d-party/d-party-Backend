"""
ASGI config for d_party project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d_party.settings")

# application = get_asgi_application()
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter

from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import OriginValidator
import streamer.routing
from . import settings

allowed_hosts = [
    "anime.dmkt-sp.jp",
    "http://anime.dmkt-sp.jp:80",
    "https://anime.dmkt-sp.jp",
    "https://anime.dmkt-sp.jp:443",
]

if settings.DEBUG:
    allowed_hosts += ["*"]


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": OriginValidator(
            AuthMiddlewareStack(URLRouter(streamer.routing.websocket_urlpatterns)),
            allowed_hosts,
        ),
    }
)
