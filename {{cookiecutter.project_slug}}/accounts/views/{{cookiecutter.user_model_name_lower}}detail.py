from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from skirmish.constants import SUCCESS_RESPONSE, ERR_PLAYER_NOT_FOUND
from accounts.models import Player
from ..permissions import isuser
from ..serializers import PlayerSerializer, PlayerUpdateSerializer


class PlayerDetail(GenericAPIView):

    permission_classes = (isuser.IsUser, permissions.IsAuthenticatedOrReadOnly)
    parser_classes = (
        FormParser,
        MultiPartParser,
    )
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    def get(self, request, pk, format=None):
        player = self.get_object()
        if player == request.user:
            serializer = PlayerUpdateSerializer(player)
        else:
            serializer = PlayerSerializer(player)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        try:
            player = Player.objects.get(id=pk)
            self.check_object_permissions(request, player)
        except Player.DoesNotExist:
            return Response(
                data={"errors": [ERR_PLAYER_NOT_FOUND]},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = PlayerUpdateSerializer(player, data=request.data, partial=True)

        if serializer.is_valid():
            player = serializer.update(player, serializer.validated_data)
            return Response(
                data=PlayerUpdateSerializer(player).data, status=status.HTTP_200_OK
            )

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
