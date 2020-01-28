from django.db import close_old_connections
from django.conf import settings
from django.contrib.auth.models import AnonymousUser

from accounts.models import Player
import jwt


class ChannelsJwtMiddleware:
    """
    Custom middleware (insecure) that takes user IDs from the query string.
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    def __call__(self, scope):
        token = scope["query_string"].decode("utf-8").split("=")
        # Look up user from query string (you should also do things like
        # check it's a valid user ID, or if scope["user"] is already populated)
        if len(token) == 0 or len(token) == 1:
            return self.inner(dict(scope, user=None))

        token = token[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = Player.objects.get(id=payload["id"])
        except (jwt.DecodeError, Player.DoesNotExist):
            user = None

        close_old_connections()

        # Return the inner application directly and let it run everything else
        return self.inner(dict(scope, user=user.id))
