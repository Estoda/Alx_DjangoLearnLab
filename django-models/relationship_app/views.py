# relationship_app/views.py

from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

def book_list_view(request):
    books = Book.objects.all()  # Query to get all books
    context = {
        'books': books,
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_object(self):
        return Library.objects.get(name = "Cairo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        books = library.books.all()
        context['books'] = books
        return context
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy
    template_name = 'relationship_app/register.html'