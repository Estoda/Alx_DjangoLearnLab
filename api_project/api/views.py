from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializer import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
