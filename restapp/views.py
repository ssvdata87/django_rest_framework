from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

from django.http import JsonResponse



class ProductListCreateView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailViewbyID(APIView):
    def get(self, request, ID):
        try:
            product = Product.objects.get(pk=ID)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

class DeleteProductbyID(APIView):
    def delete(self, request, ID):
        try:
            product = Product.objects.get(pk=ID)
            product.delete()
            return JsonResponse({'message': 'Product deleted successfully'}, status=204)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

class UpdateProductbyID(APIView):
    def put(self, request, ID):
        try:
            product = Product.objects.get(pk=ID)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
