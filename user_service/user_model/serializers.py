from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)
    gender = serializers.CharField(write_only=True)
    fullname = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'gender', 'phone', 'address', 'fullname']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = {
            'fullname': validated_data.pop('fullname', None),
            'gender': validated_data.pop('gender', None),
            'phone': validated_data.pop('phone', None),
            'address': validated_data.pop('address', None)
        }
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'gender', 'address', 'phone', 'fullname']