from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from accounts.models import {{cookiecutter.user_model_name}}
from ..serializers import {{cookiecutter.user_model_name}}Serializer


class {{cookiecutter.user_model_name}}Detail(GenericAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    parser_classes = (
        FormParser,
        MultiPartParser,
    )
    serializer_class = {{cookiecutter.user_model_name}}Serializer
    queryset = {{cookiecutter.user_model_name}}.objects.all()

    def get(self, request, pk, format=None):
        {{cookiecutter.user_model_name_lower}} = self.get_object()
        serializer = {{cookiecutter.user_model_name}}Serializer({{cookiecutter.user_model_name_lower}})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        try:
            {{cookiecutter.user_model_name_lower}} = {{cookiecutter.user_model_name}}.objects.get(id=pk)
            self.check_object_permissions(request, {{cookiecutter.user_model_name_lower}})
        except {{cookiecutter.user_model_name}}.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = {{cookiecutter.user_model_name}}Serializer({{cookiecutter.user_model_name_lower}}, data=request.data, partial=True)

        if serializer.is_valid():
            {{cookiecutter.user_model_name_lower}} = serializer.update({{cookiecutter.user_model_name_lower}}, serializer.validated_data)
            return Response(
                data={{cookiecutter.user_model_name}}Serializer({{cookiecutter.user_model_name_lower}}).data, status=status.HTTP_200_OK
            )

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
