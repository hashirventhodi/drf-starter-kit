    
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)
