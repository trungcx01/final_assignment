from rest_framework import serializers
from .models import Mobile, MobileCategory

class MobileCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileCategory
        fields = ['name', 'description']


class MobileSerializer(serializers.ModelSerializer):
    categories = MobileCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Mobile
        fields = '__all__'
