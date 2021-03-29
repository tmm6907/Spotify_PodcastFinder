from requests import Request
from rest_framework.response import Response
from rest_framework import status
from background_task import background
from finder.models import AuthToken

from .....Spotify_PodcastFinder import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from finder.serializers import ShowSerializer, EpisodeSerializer

import os

#Global Declarations
LIMIT = 50
MARKET = 'US'
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')


@background
def get_show_handler(id):
    auth = AuthToken.objects.get(id=1)
    auth = auth.access_token
    url = Request('GET', 'https://api.spotify.com/v1/shows/{id}', params= {
        'authorization': auth,
        'market': 'US',
    }).prepare().url
    return Response({'url':url}, status=status.HTTP_200_OK)

def search_shows(q,offset):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

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

                  