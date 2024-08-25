from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('books/', views.book_list, name='book_list'),
    path('example-form/', views.example_form_view, name = 'example_form'),
]