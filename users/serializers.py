from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as djoserUCS
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(djoserUCS):

    class Meta(djoserUCS.Meta):
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
            'first_name',
            'last_name'
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
        )
