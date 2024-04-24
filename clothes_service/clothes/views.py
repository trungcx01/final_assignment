import json

from django.shortcuts import get_object_or_404
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Clothes,ClothesCategory
from .serializers import ClothesSerializer, ClothesCategorySerializer


@api_view(['GET', 'POST'])
def view_clothes_categories(request):
    if request.method == 'GET':
        categories = ClothesCategory.objects.all()
        if categories:
            serializer = ClothesCategorySerializer(categories, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        category = ClothesCategorySerializer(data=request.data)
        if ClothesCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("ClothesCategory is exist!")
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def clothes_category_detail(request, pk):
    category = ClothesCategory.objects.get(pk=pk)
    if request.method == 'GET':
        if category:
            serializer = ClothesCategorySerializer(category)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        data = ClothesCategorySerializer(category, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST'])
def view_clothes(request):
    if request.method == 'GET':
        if request.query_params:
            list_clothes = Clothes.objects.filter(**request.query_params.dict())
        else:
            list_clothes = Clothes.objects.all()
        if list_clothes:
            serializer = ClothesSerializer(list_clothes, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        clothes_serializer = ClothesSerializer(data=request.data)
        if clothes_serializer.is_valid():
            clothes = clothes_serializer.save()
            _categories = json.loads(request.data.get('categories', '[]'))
            clothes.categories.set([ClothesCategory.objects.get(pk=pk) for pk in _categories])
            return Response(clothes_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(clothes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def clothes_detail(request, pk):
    clothes = Clothes.objects.get(pk=pk)
    if (request.method == 'GET'):
        serializer = ClothesSerializer(clothes)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = ClothesSerializer(clothes, data=request.data)
        if data.is_valid():
            clothes = data.save()
            _categories = json.loads(request.data.get('categories', '[]'))
            clothes.categories.set([ClothesCategory.objects.get(pk=i) for i in _categories])
            return Response(data.data, status=status.HTTP_200_OK)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        clothes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

