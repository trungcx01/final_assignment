from rest_framework import serializers
from .models import ClothesCategory, Clothes


class ClothesCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ClothesCategory
		fields = ['name', 'description']


class ClothesSerializer(serializers.ModelSerializer):
	categories = ClothesCategorySerializer(many=True, read_only=True)

	class Meta:
		model = Clothes
		fields = '__all__'