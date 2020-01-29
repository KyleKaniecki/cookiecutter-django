from datetime import datetime
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Player
from skirmish.utils import SkirmishNotifier


class PasswordReset(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            player = Player.objects.get(email=request.data['email'])
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        token = PasswordResetTokenGenerator().make_token(player)

        if player.first_name:
            name = player.first_name
        else:
            name = player.username

        body = "Dear %s, \nPlease use the following link to reset your password:\n\n" % name

        if settings.PRODUCTION:
            body += "https://skirmish.pro/password/reset/confirm/?token=" + token + '&user_id=' + str(player.id)
        elif settings.STAGING:
            body += "https://staging.skirmish.pro/password/reset/confirm/?token=" + token + '&user_id=' + str(player.id)
        else:
            body += "http://127.0.0.1:4200/password/reset/confirm/?token=" + token + '&user_id=' + str(player.id)

        body += "\n\nSincerely,\nThe Skirmish.pro team"

        SkirmishNotifier.send_email(player, subject="Password Reset - Skirmish Pro", body=body)

        return Response(status=status.HTTP_200_OK)
