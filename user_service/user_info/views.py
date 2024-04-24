from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_model.models import Profile
from user_model.serializers import ProfileSerializer


@api_view(['GET'])
def get_user_info(request):
    username = request.query_params.get('username')
    user = User.objects.filter(username=username).first()
    if user:
        profile = Profile.objects.filter(user=user).first()
        serializer_data = ProfileSerializer(profile)
        return Response(serializer_data.data, status=status.HTTP_200_OK)
    return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
