from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
def index(request):
    return HttpResponse(f"{Book.objects.all()}")