from rest_framework.response import Response
from django.db.models import Q

from skirmish.utils import (
    generate_custom_error_response,
    create_list_dataset,
    prepare_parameters,
)
from skirmish.views import SkirmishBaseListView
from ..models import Player
from ..serializers import PlayerSerializer


class PlayerList(SkirmishBaseListView):
    def get(self, request, format=None):
        players = Player.objects.filter(self.get_query_filter(request))

        page, page_length = self.get_pagination_info(request)

        return Response(
            create_list_dataset(
                [players], [PlayerSerializer], page, page_length=page_length
            )
        )

    def get_query_filter(self, request) -> Q:
        query_filter = Q()
        query_params = prepare_parameters(request.GET)

        if "username" in query_params:
            query_filter &= Q(username__icontains=query_params["username"])

        if "id" in query_params:
            query_filter &= Q(id__in=query_params["id"])

        return query_filter
