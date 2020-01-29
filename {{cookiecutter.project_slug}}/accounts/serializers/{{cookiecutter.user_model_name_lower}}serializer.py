from rest_framework import serializers

from accounts.models import {{cookiecutter.user_model_name}}


class {{cookiecutter.user_model_name}}Serializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = Player
        fields = (
            "id",
            "username",
            "is_staff",
            "is_superuser",
        )

        read_only_fields = ("is_superuser", "is_staff")
