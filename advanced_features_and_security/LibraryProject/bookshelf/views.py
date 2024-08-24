from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.shortcuts import render
from .forms import ExampleForm

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            return render(request, 'bookshelf/form_success.html')
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
