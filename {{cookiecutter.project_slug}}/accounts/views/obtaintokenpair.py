from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.serializers import JWTSerializer


class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = JWTSerializer
