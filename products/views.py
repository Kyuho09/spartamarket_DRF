from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

# Create your views here.
class ProductListView(APIView):
    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")
        
        product = Product.objects.create(title=title, content=content)
        res_json = {
            "id": product.id,
            "title": product.title,
            "content": product.content,
            "created_at": product.created_at,
            "updated_at": product.updated_at,
        }
        return Response(res_json)
    
    def get(self, request):
        products = Product.objects.all()
        res_json = []
        for product in products:
            res_json.append(
                {
                    "id": product.id,
                    "title": product.title,
                    "content": product.content,
                    "created_at": product.created_at,
                    "updated_at": product.updated_at,
                }
            )
        return Response(res_json)