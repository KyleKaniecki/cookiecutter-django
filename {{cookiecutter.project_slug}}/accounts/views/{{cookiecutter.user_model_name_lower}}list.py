from rest_framework.response import Response
from django.db.models import Q


from {{cookiecutter.project_slug}}.views import {{cookiecutter.project_name}}BaseListView
from ..models import {{cookiecutter.user_model_name}}
from ..serializers import {{cookiecutter.user_model_name}}Serializer


class {{cookiecutter.user_model_name}}List({{cookiecutter.project_name}}BaseListView):
    def get(self, request, format=None):
        {{cookiecutter.user_model_name_lower}}s = {{cookiecutter.user_model_name}}.objects.filter(self.get_query_filter(request))

        page, page_length = self.get_pagination_info(request)

        return Response(
            self.create_list_dataset(
                [{{cookiecutter.user_model_name_lower}}s], [{{cookiecutter.user_model_name}}Serializer], page, page_length=page_length
            )
        )

    def get_query_filter(self, request) -> Q:
        query_filter = Q()
        query_params = self.prepare_parameters(request.GET)

        if "username" in query_params:
            query_filter &= Q(username__icontains=query_params["username"])

        if "id" in query_params:
            query_filter &= Q(id__in=query_params["id"])

        return query_filter
