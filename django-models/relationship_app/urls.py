# relationship_app/urls.py

from django.urls import path
import views
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/', LibraryDetailView.as_view(), name = "library-detail"),
    path('login/', LoginView.as_view(template_name = '/root/10thWeek/django-models/LibraryProject/relationship_app/templates/relationship_app/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = '/root/10thWeek/django-models/LibraryProject/relationship_app/templates/relationship_app/logout.html'), name = 'logout'),
    path('register/', views.register.as_view(), name = "register")
]
