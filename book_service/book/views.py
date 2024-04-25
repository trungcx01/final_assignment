import json

from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status, serializers
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Book, BookCategory, Author, Publisher
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer, PublisherSerializer


@api_view(['GET', 'POST'])
def view_categories(request):
    if request.method == 'GET':
        categories = BookCategory.objects.all()
        if categories:
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        category = CategorySerializer(data=request.data)
        if BookCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("Category is exist!")
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    category = BookCategory.objects.get(pk=pk)
    if request.method == 'GET':
        if category:
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        data = CategorySerializer(category, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST'])
def view_authors(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        if authors:
            serializer = AuthorSerializer(authors, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        author = AuthorSerializer(data=request.data)
        if Author.objects.filter(**request.data).exists():
            raise serializers.ValidationError("Author is exist!")
        if author.is_valid():
            author.save()
            return Response(author.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == 'GET':
        if author:
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        data = AuthorSerializer(author, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST'])
def view_publishers(request):
    if request.method == 'GET':
        publisher = Publisher.objects.all()
        if publisher:
            serializer = PublisherSerializer(publisher, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        publisher = PublisherSerializer(data=request.data)
        if Publisher.objects.filter(**request.data).exists():
            raise serializers.ValidationError("Publisher is exist!")
        if publisher.is_valid():
            publisher.save()
            return Response(publisher.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def publisher_detail(request, pk):
    publisher = Publisher.objects.get(pk=pk)
    if request.method == 'GET':
        if publisher:
            serializer = PublisherSerializer(publisher)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        data = PublisherSerializer(publisher, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST'])
@parser_classes((MultiPartParser, FormParser))
def view_books(request):
    if request.method == 'GET':
        books = Book.objects.filter(**request.query_params.dict())
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book = book_serializer.save()
            _categories = json.loads(request.data.get('categories', '[]'))
            book.categories.set([BookCategory.objects.get(pk=pk) for pk in _categories])
            # categories_ids = request.data.get('categories', [])
            # book.categories.set(categories_ids)
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes((MultiPartParser, FormParser))
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = BookSerializer(book, data=request.data)
        if data.is_valid():
            book = data.save()
            _categories = json.loads(request.data.get('categories', '[]'))
            book.categories.set([BookCategory.objects.get(pk=pk) for pk in _categories])
            return Response(data.data)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def search_books_by_keywords(request):
    searched_books = Book.objects.filter(Q(title__icontains=request.query_params.get('keywords')))
    serializer = BookSerializer(searched_books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)