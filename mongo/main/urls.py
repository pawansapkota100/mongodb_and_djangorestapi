# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet,MedicineList,medicine

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')


urlpatterns = [
    path('', include(router.urls)),
    path('medicines/', MedicineList.as_view(), name='medicine-list'),
    path('medicines/<str:medicine_id>/', medicine, name='medicine-detail'),
]
