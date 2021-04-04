
from rest_framework import serializers
from .models import AuthToken

class AuthTokenSerializer(serializers.Serializer):
    class Meta:
        model = AuthToken
        fields = {
            'user',                
            'created_at',        
            'access_token',        
            'token_type',          
            'refresh_token',       
            'expires_in',          
        }
        