from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120)
    password = serializers.CharField(min_length=8)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise ValidationError("Username already exists")

class UserAuthSerializer(UserRegisterSerializer):
    pass