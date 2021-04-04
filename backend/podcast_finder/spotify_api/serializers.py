from rest_framework import serializers
from .models import Show, Episode

class ShowSerializer(serializers.Serializer):
    class Meta:
        model = Show
        fields ={
            'show_id',            
            'name',                
            'description',         
            'show_type',  
        }
             
    
class EpisodeSerializer(serializers.Serializer):
    class Meta:
        model = Episode
        fields ={
            'show_id',            
            'name',                
            'description',         
            'show_type',  
        }