from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentVeiwSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentVeiwSet)

urlpatterns = [
    path('', include(router.urls)),
]