from django.urls import path, include
from .views import NotificationListView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notifications'),
]