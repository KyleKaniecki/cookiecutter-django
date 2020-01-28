from channels.routing import ProtocolTypeRouter, URLRouter
from {{cookiecutter.project_slug}}.channels.middleware import ChannelsJwtMiddleware
from .routing import channels_paths

application = ProtocolTypeRouter(
    {"websocket": ChannelsJwtMiddleware(URLRouter(channels_paths))}
)