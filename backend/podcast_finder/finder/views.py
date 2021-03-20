from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PodcastSerializer
from .models import Podcast

import requests


# Create your views here.
class PodcastView(APIView):
    def get(self, request, *args, **kwargs):
        objs = Podcast.objects.all()
        serializer = PodcastSerializer(objs, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        id = 0
        while True:
            url = 'https://api.spotify.com/v1/shows/{id}'
            id+=1
            req = requests.get(url.format(id).json)

        serializer = PodcastSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)