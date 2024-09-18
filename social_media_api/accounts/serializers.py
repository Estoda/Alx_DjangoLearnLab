from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            return get_user_model().objects.create_user(**validated_data)
        
class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['username', 'followers']  # Users cannot change these fields
