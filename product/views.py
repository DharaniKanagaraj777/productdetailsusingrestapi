from django.shortcuts import render
from .models import ProductDetail
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework .response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def Product_list(request):
    if request.method == 'GET':
      product = ProductDetail.objects.all()
      serializer = ProductSerializer(product,many=True)
      return Response({'product':serializer.data})
    
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def Product_detail(request,pk):
    try:
        product = ProductDetail.objects.get(pk=pk)
    except ProductDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)