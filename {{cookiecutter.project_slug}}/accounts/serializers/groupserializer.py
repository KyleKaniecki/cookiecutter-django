from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    class Meta:
        model = Group
        fields = ('name',)