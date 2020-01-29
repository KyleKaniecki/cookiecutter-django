from datetime import datetime
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import {{cookiecutter.user_model_name}}


class PasswordReset(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            {{cookiecutter.user_model_name_lower}} = {{cookiecutter.user_model_name}}.objects.get(email=request.data['email'])
        except {{cookiecutter.user_model_name}}.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        token = PasswordResetTokenGenerator().make_token({{cookiecutter.user_model_name_lower}})

        if {{cookiecutter.user_model_name_lower}}.first_name:
            name = {{cookiecutter.user_model_name_lower}}.first_name
        else:
            name = {{cookiecutter.user_model_name_lower}}.username

        # Maybe send an email instead of returning the code?

        return Response(data={'token': token}, status=status.HTTP_200_OK)
