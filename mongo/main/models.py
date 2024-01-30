# models.py

from djongo import models
from django.db import IntegrityError
from rest_framework.response import Response


class Book(models.Model):
    book_id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    published_date = models.DateField()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response({"error": "Duplicate book_id. Choose a different book_id."}, status=400)


    def __str__(self):
        return self.title


    def __str__(self):
        return self.title


class Author(models.Model):
    Author_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    book= models.ForeignKey(Book, on_delete=models.CASCADE)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
