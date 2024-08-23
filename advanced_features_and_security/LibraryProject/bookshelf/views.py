from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})