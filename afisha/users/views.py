from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserAuthSerializer
from random import randint
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def authorize_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    user = authenticate(username=username, password=password)
    if user:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response({'key': token.key})

    return Response(status=status.HTTP_401_UNAUTHORIZED)


random_code = randint(100000, 999999)
print(random_code)


@api_view(['POST'])
def register_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user_code = request.data.get('user_code')

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    if user_code != random_code:
        return Response({"error": "The code is not correct."}, status=status.HTTP_403_FORBIDDEN)
    is_active = True
    user = User.objects.create_user(username=username, password=password, is_active=is_active)
    user.save()
    return Response({"user_id": user.id}, status=status.HTTP_201_CREATED)