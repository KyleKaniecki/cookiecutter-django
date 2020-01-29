from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import {{cookiecutter.user_model_name}}


class PasswordResetConfirm(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            {{cookiecutter.user_model_name_lower}} = {{cookiecutter.user_model_name}}.objects.get(id=int(request.data["id"]))
        except ({{cookiecutter.user_model_name}}.DoesNotExist, ValueError):
            return Response(status=status.HTTP_404_NOT_FOUND)

        valid = PasswordResetTokenGenerator().check_token({{cookiecutter.user_model_name_lower}}, request.data["token"])

        if valid:
            {{cookiecutter.user_model_name_lower}}.set_password(request.data["password"])
            {{cookiecutter.user_model_name_lower}}.save()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
