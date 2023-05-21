from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Product
from .serializers import ProductSerializer

@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_products(request):
    query_params = request.query_params.dict()
    
    if query_params:
        items = Product.objects.filter(**query_params)
    else:
        items = Product.objects.all()
    
    if items:
        serializer = ProductSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['PUT'])
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    serializer = ProductSerializer(product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
