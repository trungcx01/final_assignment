import json

from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mobile,MobileCategory
from .serializers import MobileSerializer, MobileCategorySerializer


@api_view(['GET', 'POST'])
def view_mobile_categories(request):
    if request.method == 'GET':
        categories = MobileCategory.objects.all()
        if categories:
            serializer = MobileCategorySerializer(categories, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        category = MobileCategorySerializer(data=request.data)
        if MobileCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("mobileCategory is exist!")
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def mobile_category_detail(request, pk):
    category = MobileCategory.objects.get(pk=pk)
    if request.method == 'GET':
        if category:
            serializer = MobileCategorySerializer(category)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        data = MobileCategorySerializer(category, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST'])
def view_mobile(request):
    if request.method == 'GET':
        if request.query_params:
            list_mobile = Mobile.objects.filter(**request.query_params.dict())
        else:
            list_mobile = Mobile.objects.all()
        if list_mobile:
            serializer = MobileSerializer(list_mobile, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        mobile_serializer = MobileSerializer(data=request.data)
        if mobile_serializer.is_valid():
            mobile = mobile_serializer.save()
            _categories = json.loads(request.data.get('categories', '[]'))
            mobile.categories.set([MobileCategory.objects.get(pk=pk) for pk in _categories])
            return Response(mobile_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(mobile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def mobile_detail(request, pk):
    mobile = Mobile.objects.get(pk=pk)
    if (request.method == 'GET'):
        serializer = MobileSerializer(mobile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = MobileSerializer(mobile, data=request.data)
        if data.is_valid():
            mobile = data.save()
            _categories = json.loads(request.data.get('categories', '[]'))
            mobile.categories.set([MobileCategory.objects.get(pk=i) for i in _categories])
            return Response(data.data, status=status.HTTP_200_OK)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        mobile.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

