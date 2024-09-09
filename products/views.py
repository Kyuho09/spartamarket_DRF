from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")
        product = Product.objects.create(title=title, content=content, user=request.user)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.user != request.user:
            return Response({"message": "해당 게시글을 수정할 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.user != request.user:
            return Response({"error": "해당 게시글을 삭제할 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        product.delete()
        return Response({"message": "게시글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
