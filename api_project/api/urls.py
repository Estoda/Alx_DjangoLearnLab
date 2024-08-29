from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter
router.register(r'BookList', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]