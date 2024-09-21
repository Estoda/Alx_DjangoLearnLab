from rest_framework import serializers
from .models import Notifications

class NotificationSerializer(serializers.ModelSerializer):
    actor_name = serializers.CharField(source='actor.username', read_only=True)
    target_object = serializers.CharField(source='target', read_only=True)

    class Meta:
        model = Notifications
        fields = '__all__'
        