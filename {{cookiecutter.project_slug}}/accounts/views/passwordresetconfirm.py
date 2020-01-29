from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skirmish.constants import (
    SUCCESS_RESPONSE,
    ERR_PLAYER_NOT_FOUND,
    ERR_TOKEN_NOT_VALID,
)
from accounts.models import Player


class PasswordResetConfirm(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            player = Player.objects.get(id=int(request.data["id"]))
        except (Player.DoesNotExist, ValueError):
            return Response(
                data={"errors": [ERR_PLAYER_NOT_FOUND]},
                status=status.HTTP_404_NOT_FOUND,
            )

        valid = PasswordResetTokenGenerator().check_token(player, request.data["token"])

        if valid:
            player.set_password(request.data["password"])
            player.save()
            return Response(data=SUCCESS_RESPONSE, status=status.HTTP_200_OK)

        return Response(
            data={"errors": [ERR_TOKEN_NOT_VALID]}, status=status.HTTP_400_BAD_REQUEST
        )
