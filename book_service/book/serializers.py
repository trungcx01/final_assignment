from rest_framework import serializers
from .models import BookCategory, Book, Author, Publisher



class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = BookCategory
		fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Publisher
		fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
	author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), allow_empty=False)
	publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all(), allow_empty=False)
	categories = CategorySerializer(many=True, read_only=True)
	class Meta:
		model = Book
		# fields = ['title', 'publisher','author','year', 'images', 'description', 'language', 'categories', 'price']
		fields = '__all__'