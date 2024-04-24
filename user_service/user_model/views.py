from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['POST'])
def registeration_view(request):
    serializer_data = UserSerializer(data= request.data)
    if serializer_data.is_valid():
        new_user = serializer_data.save()
        return Response({'message': 'Register successful!'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'Register fail!', 'error': serializer_data.errors}, status=status.HTTP_400_BAD_REQUEST)