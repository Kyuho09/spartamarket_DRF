from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductListView(APIView):
    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")
        product = Product.objects.create(title=title, content=content)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({"message": "게시글이 삭제되었습니다."}, status=204)