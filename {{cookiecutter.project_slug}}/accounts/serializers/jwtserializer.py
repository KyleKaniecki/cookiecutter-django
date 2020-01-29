from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .groupserializer import GroupSerializer


class JWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Customize the token payload
        token["username"] = user.username
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["is_superuser"] = user.is_superuser
        token["is_staff"] = user.is_staff
        token["is_active"] = user.is_active
        token["groups"] = GroupSerializer(user.groups, many=True).data

        return token
