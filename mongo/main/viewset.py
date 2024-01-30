# from rest_framework.views import APIView
# from .models import Product
# from .serializers import ProductSerializer
# from django.http.response import JsonResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.http import JsonResponse
# from .models import Product
# from .serializers import ProductSerializer

# class ProductList(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         name= request.GET.get('name', None)
#         serializer = ProductSerializer(products, many=True)
#         return JsonResponse(serializer.data, safe=False)


# class SingleProduct(APIView):
#     def get(self, request, title):
#         try:
#             product = Product.objects.get(name=title)
#             serializer = ProductSerializer(product)
#             return JsonResponse(serializer.data)
#         except Product.DoesNotExist:
#             return JsonResponse({"error": f"Product with name '{title}' not found."}, status=404)

        

# # ... other views for creating, updating, and deleting products
