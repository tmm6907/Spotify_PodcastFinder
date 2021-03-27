from django.shortcuts import render
from .searchwords import search_words
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request
from .utils import get_show_handler
from finder.serializers import PodcastSerializer

# Create your views here.

#Global variables
search_list = search_words

class SpotifyAPIView(APIView):
    def get(self, request, format = None):
        id = 0
        obj_list = {}
        while(True):
            obj = get_show_handler(id)
            obj_list['obj{index}'] += obj
            id += 1
        serializer = PodcastSerializer(data = obj_list, many = True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)