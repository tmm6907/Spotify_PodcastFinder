from requests import Request
from rest_framework.response import Response
from rest_framework import status
from background_task import background
import os
from .....Spotify_PodcastFinder import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from spotify_api.serializers import ShowSerializer, EpisodeSerializer

#Global Declarations
LIMIT = 50
MARKET = 'US'
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
#uri = os.getenv('REDIRECT_URI')

@background
def search_shows(q,offset):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

    results = sp.search(q= 'meta={q}', limit=50, offset=offset, market = MARKET, type = 'show%2Cepisode')
    for show in enumerate(results['shows']['items']):
        ds = {
            'name'              : show.name,             
            'publisher'         : show.publisher,           
            'description'       : show.description,         
            'show_type'         : show.type,   
        }
        serializer = ShowSerializer(data = ds)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
    for episode in enumerate(results['episodes']['items']):
        ds = {
            'episode_name'      : episode.name,             
            'id'                : episode.id,           
            'description'       : episode.description,         
            'show_type'         : episode.type,   
        }
        serializer = EpisodeSerializer(data = ds)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

                  