from rest_framework.response import Response
from background_task import background
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from .models import Show
from .hidden import *

#Global Declarations
LIMIT = 50
MARKET = 'US'

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')
#uri = os.getenv('REDIRECT_URI')

@background
def search_shows(q,offset):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

    results = sp.search(q= q, limit=LIMIT, offset=offset, market = MARKET, type = 'show')
    for show in results['shows']['items']:
        podcast = Show(show_id = show['id'], name = show['name'], description = show['description'], languages = show['languages'], show_type = show['type'])
        podcast.full_clean
        podcast.save()

        # if serializer.is_valid():
        #     serializer.save()
        # else:
        #     return Response(serializer.errors)
    # for episode in enumerate(results['episodes']['items']):
    #     ds = {
    #         'episode_name'      : episode.name,             
    #         'id'                : episode.id,           
    #         'description'       : episode.description,         
    #         'show_type'         : episode.type,   
    #     }
    #     serializer = EpisodeSerializer(data = ds)
    #     if serializer.is_valid():
    #         serializer.save()
    #     else:
    #         return Response(serializer.errors)

                  