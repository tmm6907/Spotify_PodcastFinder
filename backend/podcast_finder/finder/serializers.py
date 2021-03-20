
from rest_framework import Serializers
from models import Podcast

class PodcastSerializer(Serializers.serializer):
    class Meta:
        model = Podcast
        fields = {
        'name',             
        'publisher',           
        'description',         
        'show_type',           
        }