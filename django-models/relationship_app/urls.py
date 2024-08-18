# relationship_app/urls.py

from django.urls import path
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
import views
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/', LibraryDetailView.as_view(), name = "library-detail"),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name = 'logout'),
    path('register/', views.register.as_view(), name = "register"),
    path('admin/', admin_view, name='admin-view'),
    path('librarian/', librarian_view, name='librarian-view'),
    path('member/', member_view, name='member-view'),
]
