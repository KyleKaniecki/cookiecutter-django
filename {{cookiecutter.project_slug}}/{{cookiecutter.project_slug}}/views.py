from django.core.paginator import EmptyPage, InvalidPage, Page, Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.http import QueryDict
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

class {{cookiecutter.project_name}}APIView(APIView):
    def prepare_parameters(self, params: QueryDict) -> dict:
        new_params = {}
        # This converts a query dict into a normal dictionary
        # However, it preserves lists if a list of query parameters is given
        params = {k: v[0] if len(v) == 1 else v for k, v in params.lists()}

        for key, value in params.items():
            if value in ["true", "True"]:
                new_params[key] = True
            elif value in ["false", "False"]:
                new_params[key] = False
            else:
                new_params[key] = value

        return new_params

class {{cookiecutter.project_name}}BaseListView({{cookiecutter.project_name}}APIView):
    def get_query_filter(self, request) -> Q:
        raise NotImplementedError("This is an abstract method!")

    def get_pagination_info(self, request) -> (int, int):
        try:
            page = int(request.GET.get("page", 1))
        except ValueError:
            page = 1

        try:
            page_length = int(request.GET.get("page_length", 15))
        except ValueError:
            page_length = 15

        return page, page_length
    
    def create_list_dataset(self, querysets: list, serializers: list, page: int, page_length:int=25, context:dict={}):
        """Creates a formatted, paginated, standardized list dataset that we can return
        to the user

        Args:
            querysets (list): a list of querysets that will be returned in the dataset
            serializers (list): the list of serializers to use to serializer the querysets
            page (int): the page of the list
            page_length (int): The length of the page
            context (:obj:`dict`, optional): The context to hand to the serializers when they
                serializer the objects

        Returns:
            dict: A dictionary in the following format::
            {
                count: 100,
                page: 1,
                page_length: 15,
                items: []
            }

        """
        data = {"count": 0, "page_length": page_length, "items": []}

        count = 0
        obj_list = []
        for queryset, serializer in zip(querysets, serializers):
            count += len(queryset)
            obj_list.extend(serializer(queryset, context=context, many=True).data)

        paginator = Paginator(obj_list, page_length)
        try:
            p_page = paginator.page(page)
        except (InvalidPage, EmptyPage) as e:
            p_page = Page([], page, paginator)

        data["items"] = p_page.object_list
        data["count"] = count

        return data


class HealthCheck(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response()


class SchemaView(View):
    def get(self, request):
        return render(request, "schema.html")