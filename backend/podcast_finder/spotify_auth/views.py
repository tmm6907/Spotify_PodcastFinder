
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from requests import Request, post

from .serializers import AuthTokenSerializer

import os

#Global Variables
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
uri = os.environ.get('REDIRECT_URI')

# Create your views here.
class AuthURL(APIView):
    def get(self, request, format = None):
        url = Request('GET', 'https://accounts.spotify.com/authorize', params= {
            'client_id': client_id,
            'response_type': 'code',
            'redirect_uri': uri,
        }).prepare().url
        return Response({'url':url}, status=status.HTTP_200_OK)
    def getAuthToken(self, request, format=None):
        code = request.GET.get('code')
        # error = request.GET.get('error')
        response = post('https://accounts.spotify.com/api/token', data= {
            'grant-type'            : 'authorization-code',
            'code'                  : code,
            'redirect_uri'          : uri,
            'client_id'             : client_id,
            'client_secret'         : client_secret,
        }).json()
        if not request.session.exists(request.session.session_key):
            request.session.create()
        ds = {
        'user'                      : request.session.session_key,
        'access_token'              : response.get('access_token'),
        'token_type'                : response.get('token_type'),
        'refresh_token'             : response.get('refresh_token'),
        'expires_in'                : response.get('expires_in'),
        'error'                     : response.get('error'),
        }
        serializer = AuthTokenSerializer(data = ds)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)



#def is_authenticated(session):
        #serializer = PodcastSerializer(data = request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #return Response(serializer.errors)