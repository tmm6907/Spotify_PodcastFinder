
from rest_framework import serializers
from .models import Podcast, AuthToken

class ShowSerializer(serializers.Serializer):
    class Meta:
        model = Podcast
        fields = {
        'name',             
        'publisher',           
        'description',         
        'show_type',           
        }
class EpisodeSerializer(serializers.Serializer):
    class Meta:
        model = Podcast
        fields = {
        'episode_name',        
        'id',               
        'description',       
        'show_type',      
        }
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
        