from django.shortcuts import render
from .searchwords import search_words
from rest_framework.views import ListAPIView
from rest_framework.response import Response
from requests import Request
from .utils import get_show_handler
from finder.serializers import PodcastSerializer
from finder.models import AuthToken

# Create your views here.

#Global variables
search_list = search_words

class SpotifyAPIView(ListAPIView):

    def get(self, request, *args, **kwargs):
        
        return self.list(request, *args, **kwargs)