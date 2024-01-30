# views.py
from rest_framework import viewsets
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'published_date']

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']



from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import pymongo

from django.conf import settings

my_client = pymongo.MongoClient(settings.DB_NAME)



dbname = my_client['sample_medicines']
collection_name = dbname["medicinedetails"]


class MedicineList(APIView):
    def get(self, request, format=None):
        med_details = collection_name.find({})
        medicine_list = []
        for med in med_details:
            medicine_list.append({
                "medicine_id": med["medicine_id"],
                "common_name": med["common_name"],
                "scientific_name": med["scientific_name"],
                "available": med["available"],
                "category": med["category"],
            })
        return Response(medicine_list)
    
    
    def post(self, request, format=None):
        medicine_id = request.data.get("medicine_id")
        common_name = request.data.get("common_name")
        scientific_name = request.data.get("scientific_name")
        available = request.data.get("available")
        category = request.data.get("category")
        collection_name.insert_one({
            "medicine_id": medicine_id,
            "common_name": common_name,
            "scientific_name": scientific_name,
            "available": available,
            "category": category,
        })
        return Response({
            "message": "Medicine with ID '{}' has been created successfully.".format(medicine_id)
        })
    def patch(self, request, format=None):
        medicine_id = request.data.get("medicine_id")
        common_name = request.data.get("common_name")
        scientific_name = request.data.get("scientific_name")
        available = request.data.get("available")
        category = request.data.get("category")
        collection_name.update_one({"medicine_id": medicine_id}, {"$set":{
            "common_name": common_name,
            "scientific_name": scientific_name,
            "available": available,
            "category": category,
        }})
        return Response({
            "message": "Medicine with ID '{}' has been updated successfully.".format(medicine_id)
        })
    def get_queryset(self):
        common_name_filter = self.request.query_params.get('common_name', None)
        queryset = collection_name.find({})

        if common_name_filter:
            queryset = collection_name.find({'common_name': common_name_filter})

        return queryset
    

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods

@api_view(['GET'])
@require_http_methods(["GET"])
def medicine(request, medicine_id):
    if medicine_id:
        medicine_data = collection_name.find_one({"medicine_id": medicine_id})
        if medicine_data:
            medicine_info = {
                "medicine_id": medicine_data["medicine_id"],
                "common_name": medicine_data["common_name"],
                "scientific_name": medicine_data["scientific_name"],
                "available": medicine_data["available"],
                "category": medicine_data["category"],
            }
            return Response(medicine_info)
        else:
            return Response({"error": "Medicine not found"}, status=404)
    else:
        return Response({"error": "medicine_id is not provided"}, status=400)

        
    
