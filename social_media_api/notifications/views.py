from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Notifications
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notifications.objects.filter(recipient=self.request.user).order_by('-created_at')
